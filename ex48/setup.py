try:
    from setuptools import setup
    print("setuptools setup")
except ImportError:
    from distutils.core import setup
    print("distutils.core setup")
    
config = {
    'description': 'Advanced User Input - lexicon',
    'author': 'Filip Kubicz',
    'url': 'http://github.com/Qbicz',
    'download_url': 'where to download',
    'author_email': 'avenger.v14@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': [],
    'scripts': [],
    'name': 'ex48'
 }

setup(**config)
 