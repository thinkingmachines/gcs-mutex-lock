from setuptools import setup
from setuptools import find_packages

setup(name='gcs-mutex-lock',
      version='0.0.1',
      description='File-based mutex locks in Google Cloud Storage',
      url='https://github.com/thinkingmachines/',
      author='Thinking Machines',
      author_email='hello@thinkingmachin.es',
      license='Apache License 2.0',
      install_requires=[
          'backoff'
      ],
      packages=find_packages(),
      zip_safe=False)
