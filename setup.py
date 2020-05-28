
from setuptools import setup

with open("README.md", "r+") as fh:
    long_description = fh.read()

setup(name='HellFlask',
      version='0.0.5',
      description='A Simple cli to automate the creation of flask websites with python.',
      long_description=long_description,
      long_description_content_type='text/markdown',
      url='https://github.com/freazesss/hell',
      author='freazesss',
      author_email='freazesss@gmail.com',
      license='MIT',
      packages=['HellFlask'],
      zip_safe=False)
