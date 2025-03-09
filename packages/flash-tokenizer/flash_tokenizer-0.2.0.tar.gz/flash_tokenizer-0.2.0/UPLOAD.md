```bash

pip install build twine
python -m build
# pip install dist/*.whl
python -m twine upload --repository-url https://upload.pypi.org/legacy/ dist/*

```