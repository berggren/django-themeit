import os
from setuptools import setup, find_packages
import themeit


def read(fname):
    try:
        return open(os.path.join(os.path.dirname(__file__), fname)).read()
    except IOError:
        return ''


setup(
    name="themeit",
    version=themeit.__version__,
    description=read('DESCRIPTION'),
    long_description=read('README.rst'),
    keywords='theme skin middleware',
    packages=find_packages(),
    author='Johan Berggren',
    author_email='jbn@nordu.net',
    url="",
    include_package_data=True,
    test_suite='themeit.tests.runtests.runtests',
)
