#!/usr/bin/env python
# -* encoding: utf-8 *-
import os
from setuptools import setup

HERE = os.path.dirname(__file__)

try:
    long_description = open(os.path.join(HERE, 'README.rst')).read()
except IOError:
    long_description = None


setup(
    name="django-dbconn-retry-python27",
    version="0.1.6",
    packages=[
        'django_dbconn_retry',
        'django_dbconn_retry.tests',
    ],
    package_dir={
        '': '.',
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: BSD License",
        "Operating System :: POSIX",
    ],
    url="https://github.com/jdelic/django-dbconn-retry/",
    author="Jonas Maurus (@jdelic) (original), Scott Baker (python2.7 port)",
    author_email="jonas-dbconn-retry@gopythongo.com, scottb@opennetworking.org",
    maintainer="GoPythonGo.com",
    maintainer_email="info@gopythongo.com, scottb@opennetworking.org",
    description="Patch Django to retry a database connection first before failing.",
    long_description=long_description,

    install_requires=[
    ],
)
