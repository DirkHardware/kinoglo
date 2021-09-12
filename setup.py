try:
    from setuptools import setup
except:
    from distutils.core import setup

config = {
        'description': 'My Project',
        'author': 'Anderson Rolf',
        'url': 'www.end-of.us',
        'download url': "I'll figure this out later.",
        'author email': 'email.the.anderson@gmail.com',
        'version': '0.1',
        'install_requires': ['nose'],
        'packages': ['NAME'],
        'scripts': [],
        'name': 'projectname'
        }

setup(**config)
