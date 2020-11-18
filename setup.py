from setuptools import setup, find_packages

VERSION = "v1.1.2"

setup(name='zotapaysdk',
      version=VERSION,
      description='Zotapay API SDK',
      url='https://www.zotapay.com',
      author='Zotapay Technology Limited',
      author_email='open-source@zotapay.com',
      license='APACHE-2.0',
      packages=find_packages(),
      install_requires=[
          'requests',
          # TODO: Add all dependencies
      ],
      zip_safe=False)
