rm -rf dist

python3 -m pip install --upgrade build --break-system-packages
python3 -m build

python3 -m pip install --upgrade twine --break-system-packages
python3 -m twine upload --repository pypi dist/*
