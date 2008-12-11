from setuptools import setup, find_packages
import sys, os

# testing git and stuff

version = '0.1'

setup(name='tldr',
      version=version,
      description="The offline web aggregator",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='',
      author='Mike Verdone',
      author_email='mike.verdone@gmail.com',
      url='http://mike.verdone.ca/tldr/',
      license='MIT License',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=True,
      install_requires=[
          # -*- Extra requirements: -*-
          "dateutil"
      ],
      entry_points="""
      # -*- Entry points: -*-
      [console_scripts]
      tldr=tldr.rss:main
      """,
      )
