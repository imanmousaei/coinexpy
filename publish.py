# this file is intended for the developers to publish new versions

import os
from setup import version


if __name__ == '__main__':
    os.system("python3 setup.py sdist")
    os.system(f"twine upload dist/coinexpy-v{version}.tar.gz")
