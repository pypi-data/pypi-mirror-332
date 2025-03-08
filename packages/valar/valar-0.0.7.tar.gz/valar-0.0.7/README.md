valar for morghulis

# prepare
```sh
python -m pip install --upgrade pip
```
```sh
pip install --upgrade build
```
```sh
pip install twine
```

# publish
```sh
rm -r dist
```
```sh
python -m build
```
```sh
twine check dist/*
```
```sh
twine upload dist/*
```