# Necessary

Python package to enforce optional dependencies.

Install with:

```bash
pip install necessary
```

## How to Use

Simply use `necessary.necessary` to conditionally import a module.

```python
from necessary import necessary

if necessary('torch'):
    # this will raise an error if
    # torch is not installed
    import torch
```

If you want to just soft fail when a necessary module is not available (that is, have necessary return `False`), use `soft_check`:

```python
try:
    # assuming torch is not installed
    necessary('torch')
except ImportError:
    out = necessary('torch', soft_check=True)
    print(out)  # this prints False
```

If you want to request a minimum version, use `min_version`:

```python
if necessary('torch', min_version='1.12.0'):
    # this will raise an error if
    # torch is not installed or if
    # the installed version is less than 0.12.0
    import torch
```

## Issues with Pylance

If you use Pylance language server with Pyright, Pylance might complain that the imported module might be out of scope. As a workaround, combine `necessary` with `TYPE_CHECKING`:

```python
from typing import TYPE_CHECKING
from necessary import necessary

if necessary('torch') or TYPE_CHECKING:
    import torch
```
