from setuptools import setup

name = "types-fanstatic"
description = "Typing stubs for fanstatic"
long_description = '''
## Typing stubs for fanstatic

This is a [PEP 561](https://peps.python.org/pep-0561/)
type stub package for the [`fanstatic`](https://github.com/zopefoundation/fanstatic) package.
It can be used by type-checking tools like
[mypy](https://github.com/python/mypy/),
[pyright](https://github.com/microsoft/pyright),
[pytype](https://github.com/google/pytype/),
[Pyre](https://pyre-check.org/),
PyCharm, etc. to check code that uses `fanstatic`. This version of
`types-fanstatic` aims to provide accurate annotations for
`fanstatic==1.5.*`.

This package is part of the [typeshed project](https://github.com/python/typeshed).
All fixes for types and metadata should be contributed there.
See [the README](https://github.com/python/typeshed/blob/main/README.md)
for more details. The source for this package can be found in the
[`stubs/fanstatic`](https://github.com/python/typeshed/tree/main/stubs/fanstatic)
directory.

This package was tested with
mypy 1.15.0,
pyright 1.1.396,
and pytype 2024.10.11.
It was generated from typeshed commit
[`2f8de52edf627266c16b01dc2aff3e378e7b29bf`](https://github.com/python/typeshed/commit/2f8de52edf627266c16b01dc2aff3e378e7b29bf).
'''.lstrip()

setup(name=name,
      version="1.5.0.20250307",
      description=description,
      long_description=long_description,
      long_description_content_type="text/markdown",
      url="https://github.com/python/typeshed",
      project_urls={
          "GitHub": "https://github.com/python/typeshed",
          "Changes": "https://github.com/typeshed-internal/stub_uploader/blob/main/data/changelogs/fanstatic.md",
          "Issue tracker": "https://github.com/python/typeshed/issues",
          "Chat": "https://gitter.im/python/typing",
      },
      install_requires=['types-setuptools', 'types-WebOb'],
      packages=['fanstatic-stubs'],
      package_data={'fanstatic-stubs': ['__init__.pyi', 'checksum.pyi', 'compiler.pyi', 'config.pyi', 'core.pyi', 'inclusion.pyi', 'injector.pyi', 'publisher.pyi', 'registry.pyi', 'wsgi.pyi', 'METADATA.toml', 'py.typed']},
      license="Apache-2.0",
      python_requires=">=3.9",
      classifiers=[
          "License :: OSI Approved :: Apache Software License",
          "Programming Language :: Python :: 3",
          "Typing :: Stubs Only",
      ]
)
