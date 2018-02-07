from __future__ import print_function

from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand
import sys

version = '0.1.0.dev0'


def read_long_description(filename="README.rst"):
    with open(filename) as f:
        return f.read().strip()


def requirements(filename="requirements.in"):
    with open(filename) as f:
        return f.readlines()


class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest
        errcode = pytest.main(self.test_args)
        sys.exit(errcode)


# Read this article before you start doing anything here:
#
#    https://caremad.io/2013/07/setup-vs-requirement/
#
# tl;dr: setup.py is for abstract (un-pinned), high-level dependencies.
#
# requirements.txt is for pinned dependencies and is used for repeatable
# builds.

setup(
    # author='Darth Vader',
    # author_email='darth.vader@uber.com',
    description='Intentionally vulnerable toy python library',
    include_package_data=True,
    # Use `extras_require` if you want people to be able to install optional
    # dependencies for you library without requiring everyone to, e.g., `pip
    # install mycoolproject[async]`:
    # extras_require={
        # 'async': [
            # "tornado",
        # ],
    # },
    install_requires=requirements(),  # Edit these in `requirements.in`.
    tests_require=requirements('requirements-test.in'),
    cmdclass={'test': PyTest},
    license='closed',
    long_description=read_long_description(),
    name='VulnerablePythonLib',
    packages=find_packages(),
    url='gitolite@code.uber.internal:engsec/VulnerablePythonLib',
    version=version,
    zip_safe=False,
    classifiers=['Private :: Do Not Upload']
)
