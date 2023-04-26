#!/usr/bin/env python
from os.path import exists

from setuptools import Distribution, find_packages, setup

with open("README.rst") as f:
    long_description = f.read()

data_files = []
bin_files = []

class ExtensionDistribution(Distribution):
    def has_ext_modules(*args, **kwargs):
        return True


for license_path in ('docs/License.html', 'docs/LICENSE'):
    if exists(license_path):
        data_files.append(('docs', [license_path]))
        bin_files.extend(['MediaInfo.dll', 'libmediainfo.*', 'libzen.*'])
        break

distclass = ExtensionDistribution if bin_files else Distribution


setup(
    name='pymediainfo',
    author='Louis Sautier',
    author_email='sautier.louis@gmail.com',
    url='https://github.com/sbraz/pymediainfo',
    project_urls={
        "Documentation": "https://pymediainfo.readthedocs.io/",
        "Bugs": "https://github.com/sbraz/pymediainfo/issues",
    },
    description="""A Python wrapper for the mediainfo library.""",
    long_description=long_description,
    packages=find_packages(),
    namespace_packages=[],
    include_package_data=True,
    zip_safe=False,
    license='MIT',
    data_files=data_files,
    use_scm_version=True,
    python_requires=">=3.7",
    setup_requires=["setuptools_scm"],
    install_requires=["importlib_metadata; python_version < '3.8'"],
    package_data={'pymediainfo': bin_files},
    distclass=distclass,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Operating System :: POSIX :: Linux",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "License :: OSI Approved :: MIT License",
    ]
)
