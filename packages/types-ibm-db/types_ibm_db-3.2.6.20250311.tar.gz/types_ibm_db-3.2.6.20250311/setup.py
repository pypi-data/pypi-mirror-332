from setuptools import setup

name = "types-ibm-db"
description = "Typing stubs for ibm-db"
long_description = '''
## Typing stubs for ibm-db

This is a [PEP 561](https://peps.python.org/pep-0561/)
type stub package for the [`ibm-db`](https://github.com/ibmdb/python-ibmdb) package.
It can be used by type-checking tools like
[mypy](https://github.com/python/mypy/),
[pyright](https://github.com/microsoft/pyright),
[pytype](https://github.com/google/pytype/),
[Pyre](https://pyre-check.org/),
PyCharm, etc. to check code that uses `ibm-db`. This version of
`types-ibm-db` aims to provide accurate annotations for
`ibm-db==3.2.6`.

This package is part of the [typeshed project](https://github.com/python/typeshed).
All fixes for types and metadata should be contributed there.
See [the README](https://github.com/python/typeshed/blob/main/README.md)
for more details. The source for this package can be found in the
[`stubs/ibm-db`](https://github.com/python/typeshed/tree/main/stubs/ibm-db)
directory.

This package was tested with
mypy 1.15.0,
pyright 1.1.396,
and pytype 2024.10.11.
It was generated from typeshed commit
[`041580d6d64f03e8dc7b2fc0f9ff5258e91f6ffb`](https://github.com/python/typeshed/commit/041580d6d64f03e8dc7b2fc0f9ff5258e91f6ffb).
'''.lstrip()

setup(name=name,
      version="3.2.6.20250311",
      description=description,
      long_description=long_description,
      long_description_content_type="text/markdown",
      url="https://github.com/python/typeshed",
      project_urls={
          "GitHub": "https://github.com/python/typeshed",
          "Changes": "https://github.com/typeshed-internal/stub_uploader/blob/main/data/changelogs/ibm-db.md",
          "Issue tracker": "https://github.com/python/typeshed/issues",
          "Chat": "https://gitter.im/python/typing",
      },
      install_requires=[],
      packages=['ibm_db-stubs'],
      package_data={'ibm_db-stubs': ['__init__.pyi', 'METADATA.toml', 'py.typed']},
      license="Apache-2.0",
      python_requires=">=3.9",
      classifiers=[
          "License :: OSI Approved :: Apache Software License",
          "Programming Language :: Python :: 3",
          "Typing :: Stubs Only",
      ]
)
