## Tensorboard helper functions
use this package to visualize volumes on tensorboard. it creates and returns a `matplotlib` figure.

### usage
- init figure:
```python
from tensorboard_helper.volume import init_figure

```
- add rows:
```python
from tensorboard_helper.volume import fill_subplots
```

-----------
For me: 
- to update the package:
```shell script
python3 -m pip install --upgrade build
python3 -m build
python3 -m pip install --user --upgrade twine
python3 -m twine upload --repository testpypi dist/*
```
