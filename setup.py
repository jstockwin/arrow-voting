import sys
from setuptools import setup, find_packages


if sys.version_info < (3, 6):
    print(sys.stderr, "{}: need Python 3.6 or later.".format(sys.argv[0]))
    print(sys.stderr, "Your Python is {}".format(sys.version))
    sys.exit(1)


setup(
    name="arrow-voting",
    packages=find_packages(),
    version="0.0.1",
    url="https://github.com/jstockwin/arrow-voting",
    author="Jake Stockwin",
    author_email="jstockwin@gmail.com",
    include_package_data=True,
    install_requires=[],
    extras_require={
        "tests": [
            "black==19.10b0",
            "mypy==0.761",
            "nose==1.3.7",
            "pycodestyle==2.5.0",
            "pytype==2020.1.8",
        ]
    },
)
