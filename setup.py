# -*- coding: utf-8 -*-

# Copyright 2020 Oceanbolt
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import setuptools  # type: ignore

with open("README.md") as fh:
    long_description = fh.read()

setuptools.setup(
    name='oceanbolt.sdk',
    description="A Python wrapper around the Oceanbolt client API",
    # use_scm_version=True,
    # setup_requires=["setuptools_scm"],
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/oceanbolt/oceanbolt-python-sdk",
    author="Oceanbolt",
    author_email="support@oceanbolt.com",
    license="MIT",
    version='0.2.1',
    packages=setuptools.PEP420PackageFinder.find(),
    namespace_packages=('oceanbolt', 'oceanbolt.com'),
    platforms='Posix; MacOS X; Windows',
    include_package_data=True,
    install_requires=(
        'google-api-core[grpc] >= 1.22.2, < 2.0.0dev',
        'libcst >= 0.2.5',
        'proto-plus >= 1.4.0',
        'pandas>=1.1.4',
        'numpy>=1.19.0',
    ),
    python_requires='>=3.6',
    scripts=[
        'scripts/fixup_portcalls_v3_keywords.py',
        'scripts/fixup_tonnage_v3_keywords.py',
        'scripts/fixup_tradeflows_v3_keywords.py',
        'scripts/fixup_drydock_v3_keywords.py',
        'scripts/fixup_entities_v3_keywords.py',
        'scripts/fixup_congestion_v3_keywords.py',
        'scripts/fixup_polygonmanagement_v3_keywords.py',
        'scripts/fixup_fleetmanagement_v3_keywords.py',
        'scripts/fixup_distancecalculator_v3_keywords.py',
        'scripts/fixup_custompolygon_v3_keywords.py',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Internet',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    zip_safe=False,
    extras_require={
        "docs": [
            "Sphinx==3.3.1",
            "sphinx_rtd_theme==0.5.1",
            "sphinx-autodoc-typehints==1.11.1",
        ],
        "test": [
            "black==18.9b0",
            "mypy-extensions==0.4.3",
            "mypy==0.782",
            "pre-commit==2.6.0",
            "pytest==5.0.0",
            "pytest-dotenv==0.5.2",
            "python-dateutil==2.8.1",
            "pytest-rerunfailures==9.1.1",
            "mock==4.0.3",
            "flake8==3.8.4",
            "hypothesis==6.8.1"
        ],
        "publish": [
            "build==0.3.0",
            "twine==3.2.0",
        ],
    },
)
