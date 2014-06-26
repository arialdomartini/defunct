import os
from setuptools import setup
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "defunct",
    version = "0.0.1",
    author = "Arialdo Martini",
    author_email = "arialdomartini@gmail.com",
    description = ("A interpreted functional programming language, highly inspired (if not shamelessly plagiarised) by LISP"),
    license = "GPL2",
    keywords = "lisp python",
    url = "https://github.com/arialdomartini/defunct",
    packages=find_packages(),
    install_requires = [''],
    tests_require = ['sure==1.2.5'],
    extras_require = {'tests': ['sure==1.2.5']},
    test_suite = "tests",
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: GPL2 License",
    ],
)
