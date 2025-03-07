### Nuthon Distribution
 while in the 'python_distribution' folder

# build the project into a package with
python3 -m build

# test-upload the package to (testpypi) with
python3 -m twine upload --repository testpypi dist/*

# upload the package to (pypi) with
python3 -m twine upload dist/*

don't forget to incremente the version before build
also remove the older build or upload only the newer version
