#-*- coding: utf-8 -*-

from distutils.core import setup
from combpy import get_version


setup(
    name='combpy',
    version=get_version(),
    description='Combinatorics-related functions.',
    long_description='Please see the Github page for details: '
                     'http://github.com/modocache/combpy',
    keywords='combinatorics permutations',
    author='modocache',
    author_email='modocache@gmail.com',
    url='http://github.com/modocache/combpy',
    packages=[
        'combpy'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Scientific/Engineering :: Mathematics',
    ]
)

