python3.10 -m pip uninstall coslab-core
rm -rf dist/*
python3.10 -m build
#python3.10 -m pip install dist/coslab_core-0.9.1-py3-none-any.whl
python3.10 -m pip install dist/coslab_core-0.9.3-py3-none-any.whl
#rm -rf dist/*
