#!/usr/bin/env python

import os
import sys
from fnmatch import fnmatch

from numpy import get_include as numpy_includes
from setuptools import setup, Extension
import sysconfig

def c_sources(parent):
    sources = []
    for root, _, files in os.walk(parent):
        for f in files:
            fn = os.path.join(root, f)
            if fnmatch(fn, '*.c'):
                sources.append(fn)
    return sources


def c_includes(parent, depth=1):
    includes = [parent]
    for root, dirs, _ in os.walk(parent):
        for d in dirs:
            dn = os.path.join(root, d)
            if len(dn.split(os.sep)) - 1 > depth:
                continue
            includes.append(dn)
    return includes


SOURCES = c_sources('src')
INCLUDES = c_includes('include') + c_includes('src') + [numpy_includes()]

cfg = {
    'libraries': [],
    'define_macros': [],
    'extra_compile_args': [],
}

if sys.platform == 'win32':
    cfg['define_macros'].append(('__STDC__', 1))
    cfg['define_macros'].append(('_CRT_SECURE_NO_WARNINGS', None))
else:
    cfg['define_macros'].append(('NDEBUG', None))
    cfg['libraries'].append('m')
    cfg['extra_compile_args'] += [
        '-Wall',
        '-Wextra',
        '-Wpedantic',
        '-Wno-unused-parameter',
        '-Wincompatible-pointer-types'
    ]

# importing these extension modules is tested in `.github/workflows/build.yml`;
# when adding new modules here, make sure to add them to the `test_command` entry there
ext_modules = [
    Extension(
        'stsci.stimage._stimage',
        sources=SOURCES,
        include_dirs=INCLUDES,
        **cfg,
    ),
]

setup(
    ext_modules=ext_modules,
)
