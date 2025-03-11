from setuptools import setup

name = "types-geopandas"
description = "Typing stubs for geopandas"
long_description = '''
## Typing stubs for geopandas

This is a [PEP 561](https://peps.python.org/pep-0561/)
type stub package for the [`geopandas`](https://github.com/geopandas/geopandas) package.
It can be used by type-checking tools like
[mypy](https://github.com/python/mypy/),
[pyright](https://github.com/microsoft/pyright),
[pytype](https://github.com/google/pytype/),
[Pyre](https://pyre-check.org/),
PyCharm, etc. to check code that uses `geopandas`. This version of
`types-geopandas` aims to provide accurate annotations for
`geopandas==1.0.1`.

This package is part of the [typeshed project](https://github.com/python/typeshed).
All fixes for types and metadata should be contributed there.
See [the README](https://github.com/python/typeshed/blob/main/README.md)
for more details. The source for this package can be found in the
[`stubs/geopandas`](https://github.com/python/typeshed/tree/main/stubs/geopandas)
directory.

This package was tested with
mypy 1.15.0,
pyright 1.1.396,
and pytype 2024.10.11.
It was generated from typeshed commit
[`59717f4d0a24beb43dfff81041bf2ee70895d3a8`](https://github.com/python/typeshed/commit/59717f4d0a24beb43dfff81041bf2ee70895d3a8).
'''.lstrip()

setup(name=name,
      version="1.0.1.20250310",
      description=description,
      long_description=long_description,
      long_description_content_type="text/markdown",
      url="https://github.com/python/typeshed",
      project_urls={
          "GitHub": "https://github.com/python/typeshed",
          "Changes": "https://github.com/typeshed-internal/stub_uploader/blob/main/data/changelogs/geopandas.md",
          "Issue tracker": "https://github.com/python/typeshed/issues",
          "Chat": "https://gitter.im/python/typing",
      },
      install_requires=['types-shapely', 'numpy>=1.20', 'pandas-stubs', 'pyproj'],
      packages=['geopandas-stubs'],
      package_data={'geopandas-stubs': ['__init__.pyi', '_config.pyi', '_decorator.pyi', '_exports.pyi', 'array.pyi', 'base.pyi', 'explore.pyi', 'geodataframe.pyi', 'geoseries.pyi', 'io/__init__.pyi', 'io/_geoarrow.pyi', 'io/arrow.pyi', 'io/file.pyi', 'io/sql.pyi', 'plotting.pyi', 'sindex.pyi', 'testing.pyi', 'tools/__init__.pyi', 'tools/_show_versions.pyi', 'tools/clip.pyi', 'tools/geocoding.pyi', 'tools/hilbert_curve.pyi', 'tools/overlay.pyi', 'tools/sjoin.pyi', 'tools/util.pyi', 'METADATA.toml', 'py.typed']},
      license="Apache-2.0",
      python_requires=">=3.9",
      classifiers=[
          "License :: OSI Approved :: Apache Software License",
          "Programming Language :: Python :: 3",
          "Typing :: Stubs Only",
      ]
)
