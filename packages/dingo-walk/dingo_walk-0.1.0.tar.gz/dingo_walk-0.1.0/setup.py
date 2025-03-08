# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['dingo_walk', 'dingo_walk.experimental_gurobi_functions']

package_data = \
{'': ['*'], 'dingo_walk': ['bindings/*']}

install_requires = \
['Cython>=0.29.22,<0.30.0',
 'argparse>=1.4.0,<2.0.0',
 'cobra>=0.26.0,<0.27.0',
 'kaleido==0.2.1',
 'matplotlib>=3.4.1,<4.0.0',
 'numpy>=1.20.1,<2.0.0',
 'plotly>=5.11.0,<6.0.0',
 'scipy>=1.6.1,<2.0.0',
 'simplejson>=3.17.2,<4.0.0',
 'sparseqr>=1.2.1,<2.0.0']

setup_kwargs = {
    'name': 'dingo-walk',
    'version': '0.1.0',
    'description': 'High dimensional polytope sampling in Python. dingo_walk comes with a set of tools for metabolic network sampling and analysis. dingo_walk is part of GeomScale project.',
    'long_description': 'None',
    'author': 'Apostolos Chalkis',
    'author_email': 'tolis.chal@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}
from build import *
build(setup_kwargs)

setup(**setup_kwargs)
