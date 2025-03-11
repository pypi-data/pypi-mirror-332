<!-- SPDX-FileCopyrightText: 2025 Tymoteusz Blazejczyk <tymoteusz.blazejczyk@tymonx.com> -->
<!-- SPDX-License-Identifier: Apache-2.0 -->

# PyTCL

**PyTCL** allows control **EDA** tools directly from **Python** that use **TCL**.

## Features

- It executes Python method with provided positional arguments directly as TCL procedure
  For example invocation of Python `<object>.<name>(*args)` method is like calling TCL procedure `<name> {*}${args}`
- Any Python value is converted to TCL value like for example Python `list` to TCL list
- Result from invoked TCL procedure is returned as `pytcl.TCLValue` that can handle any TCL value
  (that is represented always as string) to Python `str`, `int`, `bool`, `float`, `list`, `dict`, ...
- TCL error is returned as Python exception `pytcl.TCLError`
- High performance and very low (unnoticeable) overhead by using Unix domain sockets for communication
  between Python and TCL in streamable way (sockets are always open and ready)
- It allows to create and access TCL variables from Python side. Please see [tests/test_tclsh.py] for some examples
- It can work with any EDA tool. Please see [tests/test_vivado.py] how to use bare `PyTCL` class for that
- No external dependencies

## Install

```python
pip install pytcl-eda
```

## Examples

Creating new Vivado project:

```python
#!/usr/bin/env python3
from pathlib import Path
from pytcl import Vivado

def main() -> None:
    """Create new Vivado project."""
    hdl_dir: Path = Path.cwd() / "hdl"
    project_dir: Path = Path.cwd() / "my-awesome-project"

    with Vivado() as vivado:
        # See Vivado Design Suite Tcl Command Reference Guide (UG835) for all available Vivado TCL procedures
        # https://docs.amd.com/r/en-US/ug835-vivado-tcl-commands
        vivado.create_project(project_dir.name, project_dir)

        vivado.add_files(hdl_dir / "my_awesome_design.sv")

        synthesis_runs = list(vivado.get_runs("synth_*"))
        implementation_runs = list(vivado.get_runs("impl_*"))

        vivado.launch_runs(synthesis_runs)

        # wait_on_runs was introduced in Vivado 2021.2. For backward compatibility we will use wait_on_run
        # https://docs.amd.com/r/2021.2-English/ug835-vivado-tcl-commands/wait_on_runs
        # Vivado >= 2021.2 can just use: vivado.wait_on_runs(synthesis_runs)
        for run in synthesis_runs:
            vivado.wait_on_run(run)

        vivado.launch_runs(implementation_runs)

        for run in implementation_runs:
            vivado.wait_on_run(run)

        vivado.close_project()

if __name__ == "__main__":
    main()
```

To use any EDA tool where `PyTCL` doesn't provide neat helper classes like `pytcl.Vivado`
you can use the `pytcl.PyTCL` class directly:

```python
#!/usr/bin/env python3
from pathlib import Path
from pytcl import PyTCL

def main() -> None:
    """Create new Vivado project."""
    project_dir: Path = Path.cwd() / "my-awesome-project"

    # PyTCL offers some string placeholders {} that you can use:
    # {tcl}      -> it will insert <pytcl>/execute.tcl
    # {receiver} -> it will insert <pytcl>/receiver.tcl
    # {rx}       -> it will insert /tmp/pytcl-XXXXX/rx.sock
    # {sender}   -> it will insert <pytcl>/sender.tcl
    # {tx}       -> it will insert /tmp/pytcl-XXXXX/tx.sock
    # {args}     -> it will insert '{receier} {rx} {sender} {tx}' in one go
    cmd: list[str] = [
        "vivado",
        "-nojournal",
        "-notrace",
        "-nolog",
        "-mode",
        "batch",
        "-source",
        "{tcl}",
        "-tclargs",
        "{receiver}",
        "{rx}",
        "{sender}",
        "{tx}",
    ]

    with PyTCL(*cmd) as vivado:
        vivado.create_project(project_dir.name, project_dir)

        # Do the same magic that you would normally do in TCL

        vivado.close_project()

if __name__ == "__main__":
    main()
```

## Architecture

```mermaid
stateDiagram-v2
    direction LR
    PyTCL --> rx.sock: send()
    rx.sock --> receiver.py: string
    state tool {
        receiver.py --> execute.tcl: stdin
        execute.tcl --> sender.py: stdout
    }
    sender.py --> tx.sock: NDJSON
    tx.sock --> PyTCL: recv()
```

- `PyTCL` will start new receiver listened on Unix domain socket `/tmp/pytcl-XXXX/tx.sock` for any
  incoming [NDJSON] messages `{"result": "<tcl-result>", "status": <tcl-status>}` from `execute.tcl` script file
- `PyTCL` will call command line tool (by default `tclsh`) with `execute.tcl` script file and
  arguments `receiver.py /tmp/pytcl-XXXX/rx.sock sender.py /tmp/pytcl-XXXX/tx.sock`
- Started `execute.tcl` will create own listener with Unix domain socket `/tmp/pytcl-XXXX/rx.sock` to
  receive incoming TCL expressions from `PyTCL`
- `PyTCL` will start new client and connect to Unix domain socket `/tmp/pytcl-XXXX/rx.sock` to send
  TCL expressions with arguments to be evaluated by `execute.tcl` script file
- `PyTCL` will transform any Python method call `<object>.<name>(*args)` to TCL expression `<name> {*}${args}`
- `PyTCL` will send TCL expression to `execute.tcl` using Unix domain socket `/tmp/pytcl-XXXX/rx.sock`
- `execute.tcl` will receive TCL expressions from Unix domain socket `/tmp/pytcl-XXXX/rx.sock`
- Received TCL expression is evaluated by TCL `eval` within TCL `catch`
- TCL result and status from evaluated TCL expression will be packed into [NDJSON] message
  `{"result": "<tcl-result>", "status": <tcl-status>}`
- Packed [NDJSON] message with TCL result and status will be send back to `PyTCL`
- `PyTCL` will return received [NDJSON] message as `pytcl.TCLValue`
- `PyTCL` will raise a Python exception `pytcl.TCLError` if received TCL status was non-zero

## Development

Create [Python virtual environment]:

```plaintext
python3 -m venv .venv
```

Activate created [Python virtual environment]:

```plaintext
. .venv/bin/activate
```

Upgrade [pip]:

```plaintext
pip install --upgrade pip
```

Install project in [editable mode] with [pytest]:

```plaintext
pip install --editable .[test]
```

Run tests:

```plaintext
pytest
```

[ndjson]: https://docs.python.org/3/library/venv.html
[python virtual environment]: https://docs.python.org/3/library/venv.html
[editable mode]: https://setuptools.pypa.io/en/latest/userguide/development_mode.html
[pytest]: https://docs.pytest.org/en/stable/
[pip]: https://pip.pypa.io/en/stable/
[tests/test_tclsh.py]: https://gitlab.com/tymonx/pytcl/-/blob/main/tests/test_tclsh.py
[tests/test_vivado.py]: https://gitlab.com/tymonx/pytcl/-/blob/main/tests/test_vivado.py
