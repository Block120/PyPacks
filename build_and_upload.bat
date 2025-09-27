@echo off
REM Build the package
python setup.py sdist bdist_wheel

REM Upload the package to PyPI
python -m twine upload dist/*
