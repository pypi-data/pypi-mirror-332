import codecs
import os

from setuptools import find_packages, setup

# these things are needed for the README.md show on pypi
here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()


VERSION = '0.1.1'
DESCRIPTION = 'A transformation tool between IFC and IDA that supports Windows, MacOS, and Linux'
LONG_DESCRIPTION = 'A transformation tool between IFC and IDA Supporting Windows, MacOS, and Linux. It has support for hotkeys'

# Setting up
setup(
    name="IFC2IDA",
    version=VERSION,
    author="yijzq",
    author_email="W_yQ2020@163.com",
    description="A Python tool for converting IFC (Industry Foundation Classes) files to IDA (Indoor Database ASCII) compatible formats",
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=[
        'getch; platform_system=="Unix"',
        'getch; platform_system=="MacOS"',
    ],
    keywords=['python', 'IFC', 'IDA', 'windows', 'mac', 'linux'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3.12",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)