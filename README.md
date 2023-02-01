# Necessary

Python package that can be used to enforce optional dependencies are installed when a module is imported. Necessary stands for "Now Ensures Correct Existence of Select Software, or Add Resource Yourself!"

Necessary is available on [PyPI](https://pypi.org/project/necessary/), and can be installed with the following command:

```bash
pip install necessary
```

## How to Use

### As Context Manager

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

If you want to request a minimum version, use Python's requirements syntax:

```python
with necessary('torch>=1.12.0'):
    # this will raise an error if
    # torch is not installed or if
    # the installed version is less than 0.12.0
    import torch
```

You can also check multiple packages in the same `necessary` call, or combine multiple requirements:

```python
with necessary(['torch>=1.12.0', 'numpy>=1.20,<1.25']):
    # this will raise an error if torch >= 1.12.0 or numpy are not installed
    import torch
    import numpy
```

Finally, we can customize the message that is raised if a necessary module is not installed; use `{module_name}` and `{module_version}` to insert the module name and version respectively.

```python
with necessary('torch', message='I am missing {module_name}/{module_version}'):
    import torch
```

### As Function or Class Decorator

You can also use `necessary` as a function or class decorator:

```python

from necessary import Necessary

# decorating a function
@Necessary('torch')
def my_function():
    import torch

# decorating a class
@Necessary('torch')
class MyClass:
    def __init__(self):
        import torch
```

All of the same functionality is available in the decorator form as in the context manager form.
