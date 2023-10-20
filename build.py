import re
import os.path
from setuptools import setup, find_packages

with open(os.path.join(os.path.dirname(__file__), 'yourapplication', '__init__.py')) as init_py:
    VERSION = re.search("VERSION = '([^']+)'", init_py.read()).group(1)

setup(
    name='index',
    version=VERSION,
    description='Freezes your Flask application into a set of static files.',
    packages=find_packages(),
    package_data={'': ['templates/*', 'static/*']},
    install_requires=[
        'Flask',
        'Frozen-Flask'
    ],
    entry_points={
        'console_scripts': [
            'freeze=index.freeze:main'
        ]
    }
)
