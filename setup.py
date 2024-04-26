from setuptools import setup, find_packages

# Package version
VERSION = "1.2.1"

setup(
    name='zotasdk',
    version=VERSION,
    description='Zota API SDK',
    url='https://pypi.org/p/zotasdk',
    author='Zota Technology Pte Ltd',
    author_email='open-source@zota.com',
    license='APACHE-2.0',
    packages=find_packages(),
    install_requires=['requests'],
    zip_safe=False
)
