try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
'description': 'penaltyGame',
'author': 'Maksim Lebedev',
'url': 'URL to get it at.',
'download_url': 'Where to download it.',
'author_email': 'miskamvedebel@gmail.com',
'version': '0.1',
'install_requires': ['nose'],
'packages': ['penaltyGame'],
'scripts': [],
'name': 'penaltyGame'
}
setup(**config)
