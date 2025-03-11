# BUILD instructions

~~~bash
pip install build twine

# set version
git tag 0.9.0
git push --tags

# build
python -m build
# check 
twine check dist/*
# upload to PyPI
twine upload --verbose dist/*

~~~

The following error:

> Checking dist/soft_comp-XXX.whl: ERROR    InvalidDistribution: Invalid distribution metadata: unrecognized or malformed field 'license-file'               

can be fixed with:

~~~bash
pip install -U packaging 
~~~

[src](https://github.com/pypa/twine/issues/1216#issuecomment-2606531615)