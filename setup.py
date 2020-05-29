
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

# Load the version number from __init__.py
__version__ = "Undefined"
for line in open('scaffold/__init__.py'):
    if (line.startswith('__version__')):
        exec(line.strip())

config = {
    'description': 'Simple project scaffolding for Python',
    'author': 'Aaron Stannard',
    'url': 'https://github.com/Aaronontheweb/scaffold-py',
    'download_url': 'https://github.com/Aaronontheweb/scaffold-py/archive/v0.1.5.tar.gz',
    'author_email': 'aaron@stannardlabs.com',
    'version': __version__,
    'tests_require': ['nose'],
    'install_requires': [],
    'packages': ['scaffold'],
    'scripts': [],
    'name': 'Scaffold',
    'entry_points': {
        'console_scripts': [
            'pyscaffold = scaffold.__main__:main',
        ],
        'virtualenvwrapper.project.template': [
            'base = scaffold.virtualenvwrapper:template',
        ],
    }
}

setup(**config)
