#!/bin/sh
python setup.py sdist -d dist/
python setup.py bdist_wheel -d dist/
rm -rf build
rm -rf *.egg-info

# 2to3 --output-dir=src_python3/ -W -n src/
# python3 src_python3/setup.py bdist_wheel -d dist/
# rm -rf build
# rm -rf *.egg-info

gpg --detach-sign --default-key 237B0E4F -a dist/*.tar.gz

# twine upload dist/*