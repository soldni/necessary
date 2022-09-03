# Necessary

Python package that can be used to enforce optional dependencies are installed when a module is imported. Necessary stads for "Now Ensures Correct Existence of Select Software, or Add Resource Yourself!" 

Install with:

```bash
pip install necessary
```

## How to Use

Simply use `necessary.necessary` to get a context manager import a module.

```python
from necessary import necessary

with necessary('torch'):
    # this will raise a nicely written error if
    # torch is not installed
    import torch
```

If you want to just soft fail when a necessary module is not available (that is, have necessary return `False`), use `soft`:

```python
try:
    # assuming torch is not installed
    necessary('torch')
except ImportError:
    out = necessary('torch', soft=True)
    assert out is False
```

If you want to request a minimum version, use `min_version`:

```python
with necessary(('torch', '1.12.0')):
    # this will raise an error if
    # torch is not installed or if
    # the installed version is less than 0.12.0
    import torch
```

You can also check multiple packages in the same `necessary` call:

```python
with necessary([('torch', '1.12.0'), 'numpy']):
    # this will raise an error if torch >= 1.12.0 or numpy are not installed
    import torch
    import numpy
```

Finally, we can customize the message that is raised if a necessary module is not installed; use `{module_name}` and `{module_version}` to insert the module name and version respectively.

```python
with necessary('torch', message='I am missing {module_name}/{module_version}'):
    import torch
```
