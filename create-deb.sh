#! /bin/bash -ex

# dependencies
sudo apt update
sudo apt install -y python-stdeb

cd main
python setup.py --command-packages=stdeb.command sdist_dsc
cd deb_dist/cs-academic-fair-17.03.24 && dpkg-buildpackage -rfakeroot -uc -us
cd ../../
