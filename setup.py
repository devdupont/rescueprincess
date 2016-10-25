#!/usr/bin/python3

from setuptools import setup

# To create a new tarball on github, run:
#    git tag 0.1 -m "Creating tag for version 0.1"
#    git push --tags origin master
#
# See http://peterdowns.com/posts/first-time-with-pypi.html for more pypi info

# For security, run: chmod g-wx,o-wx ~/.python-eggs

setup(name='rescueprincess',
      version='0.1',
      description='Rescues the princess',
      url='https://github.com/flyinactor91/rescueprincess',
      author='Michael duPont',
      author_email='michael@mdupont.com',
      packages=[
          'rescueprincess'
      ]
     )
