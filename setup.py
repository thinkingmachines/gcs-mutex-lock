from setuptools import setup
from setuptools import find_packages

setup(name='gcs-file-lock',
      version='0.0.1',
      description='File locks in Google Cloud Storage',
      url='https://github.com/thinkingmachines/ml-tools',
      author='Thinking Machines',
      author_email='hello@thinkingmachin.es',
      license='Apache License 2.0',
      install_requires=[
          backoff
      ],
      packages=find_packages(),
      zip_safe=False)
