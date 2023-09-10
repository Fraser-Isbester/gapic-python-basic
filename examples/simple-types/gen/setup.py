# -*- coding: utf-8 -*-

import io
import os
import setuptools  # type: ignore


version = '0.0.1'

package_root = os.path.abspath(os.path.dirname(__file__))

readme_filename = os.path.join(package_root, 'README.rst')
with io.open(readme_filename, encoding='utf-8') as readme_file:
    readme = readme_file.read()

setuptools.setup(
    name='simple_types',
    version=version,
    long_description=readme,
    packages=setuptools.PEP420PackageFinder.find(),
    platforms='Posix; MacOS X; Windows',
    include_package_data=True,
    install_requires=(
        'google-api-core[grpc]',
        'googleapis-common-protos >= 1.52.0, <2.0.0dev',
        'proto-plus >= 1.19.7',
    ),
    python_requires='>=3.9',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Topic :: Internet',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    zip_safe=False,
)
