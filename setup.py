""" Setup file for fmn.web """

import sys
import os
import logging

from setuptools import setup

# Ridiculous as it may seem, we need to import multiprocessing and logging here
# in order to get tests to pass smoothly on python 2.7.
try:
    import multiprocessing
    import logging
except:
    pass


def get_description():
    with open('README.rst', 'r') as f:
        return ''.join(f.readlines()[2:])


def get_requirements(filename='requirements.txt'):
    """
    Get the contents of a file listing the requirements.

    :param filename: path to a requirements file
    :type  filename: str

    :returns: the list of requirements
    :return type: list
    """
    with open(filename) as f:
        return [
            line.rstrip().split('#')[0]
            for line in f.readlines()
            if not line.startswith('#')
        ]


setup(
    name='fmn.web',
    version='0.8.1',
    description='Frontend Web Application for Fedora Notifications',
    long_description=get_description(),
    author='Ralph Bean',
    author_email='rbean@redhat.com',
    url="https://github.com/fedora-infra/fmn.web/",
    download_url="https://pypi.python.org/pypi/fmn.web/",
    license='LGPLv2+',
    install_requires=get_requirements(),
    tests_require=get_requirements('tests-requirements.txt'),
    test_suite='nose.collector',
    packages=['fmn', 'fmn.web'],
    namespace_packages=['fmn'],
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Environment :: Web Environment',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
    ],
)
