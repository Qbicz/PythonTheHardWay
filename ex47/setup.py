try:
    from setuptools import setup
    print("setuptools setup")
except ImportError:
    from distutils.core import setup
    print("distutils.core setup")
    
config = {
    'description': 'My Project ex47',
    'author': 'Filip Kubicz',
    'url': 'url to get it all',
    'download_url': 'where to download',
    'author_email': 'avenger.v14@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['NAME'],
    'scripts': [],
    'name': 'ex47'
 }

setup(**config)
 