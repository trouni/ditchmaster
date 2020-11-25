from setuptools import find_packages
from setuptools import setup

with open('requirements.txt') as f:
    content = f.readlines()
requirements = [x.strip() for x in content if 'git+' not in x]

setup(name='roninrepo',
      version="0.1",
      description="Replace master branch with main",
      packages=find_packages(),
      scripts=['roninrepo'],
      zip_safe=False)
