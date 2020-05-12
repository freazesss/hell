
from setuptools import setup
from os import path

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name='HellFlask',
      version='0.0.3',
      description='Automate the creation of flask websites.',
      long_description=long_description,
      long_description_content_type='text/markdown',
      url='https://github.com/freazesss/hell',
      author='freazesss',
      author_email='freazesss@gmail.com',
      license='MIT',
      packages=['HellFlask'],
      zip_safe=False)
