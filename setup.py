from setuptools import setup, find_packages

# Package version
VERSION = "v1.1.4"

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
