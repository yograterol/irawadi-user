import os
import sys

from setuptools import setup, find_packages

sys.path.append('.')
from irawadi_user import metadata


def read(filename):
    with open(os.path.join(os.path.dirname(__file__), filename)) as f:
        return f.read()


# See here for more options:
# <http://pythonhosted.org/setuptools/setuptools.html>
setup_dict = dict(
    name=metadata.package,
    version=metadata.version,
    author=metadata.authors[0],
    author_email=metadata.emails[0],
    maintainer=metadata.authors[0],
    maintainer_email=metadata.emails[0],
    url=metadata.url,
    description=metadata.description,
    long_description=read('README.rst'),
    download_url=metadata.url,
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GPL License',
        'Natural Language :: English',
        'Operating System :: Linux (CentOS)',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Topic :: Documentation',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    packages=find_packages(),
    zip_safe=False  # don't use eggs
)


def main():
    setup(**setup_dict)


if __name__ == '__main__':
    main()
