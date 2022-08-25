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
if necessary(('torch', '1.12.0')):
    # this will raise an error if
    # torch is not installed or if
    # the installed version is less than 0.12.0
    import torch
```

You can also check multiple packages in the same `necessary` call::

```python
if necessary([('torch', '1.12.0'), 'numpy']):
    # this will raise an error if torch >= 1.12.0 or numpy are not installed
    import torch
    import numpy
```

Finally, we can customize the message that is raised if a necessary module is not installed; use `{module_name}` and `{module_version}` to insert the module name and version respectively.

```python
if necessary('torch', message='I am missing {module_name}/{module_version}'):
    import torch
```
