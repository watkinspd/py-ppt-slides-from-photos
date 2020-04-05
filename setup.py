from setuptools import setup
setup(
    name = 'photoslides',
    version = '0.1.0',
    packages = ['photoslides'],
    entry_points = {
        'console_scripts': [
            'photoslides = photoslides.__main__:main'
        ]
    })