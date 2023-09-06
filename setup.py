from setuptools import setup
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='did-api',
    version='0.0.3',
    description='D-ID API Python Library',
    author= 'Shubham Gupta',
    author_email='gshubham533@gmail.com',
    url = 'https://github.com/Circuit-Minds/d-id',
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    keywords=['D ID API','text to video', 't2s', 'D ID Python library'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    py_modules=['D_ID'],
    package_dir={'':'src'},
    install_requires = [
        'requests'
    ]
)