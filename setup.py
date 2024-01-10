from setuptools import setup, find_packages

# Package version
VERSION = "1.1.6"

setup(name='zotasdk',
    version=VERSION,
    description='Zotapay API SDK',
    url='https://www.zota.com',
    author='Zota Technology Pte Ltd',
    author_email='open-source@zota.com',
    license='APACHE-2.0',
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
    zip_safe=False)
