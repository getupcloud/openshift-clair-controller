from setuptools import find_packages, setup
import subprocess

PACKAGE_NAME = subprocess.run(['python', 'scripts/constants.py', 'PACKAGE_NAME'], stdout=subprocess.PIPE, encoding='utf-8').stdout.strip()
PACKAGE_VERSION = subprocess.run(['python', 'scripts/constants.py', 'PACKAGE_VERSION'], stdout=subprocess.PIPE, encoding='utf-8').stdout.strip()
DEVELOPMENT_STATUS = "3 - Alpha"

with open('requirements.txt') as f:
    REQUIRES = f.readlines()

print('Building {}-{}'.format(PACKAGE_NAME, PACKAGE_VERSION))

setup(
    name=PACKAGE_NAME,
    version=PACKAGE_VERSION,
    description="Openshift Clair Controller",
    author_email="mateus.caruccio@getupcloud.com",
    author="Mateus Caruccio",
    license="Apache License Version 2.0",
    url="https://github.com/caruccio/client-python",
    install_requires=REQUIRES,
    packages=find_packages(exclude=['scripts']),
    entry_points={
        'console_scripts': [
            'clair-controller=claircontroller.command_line:main',
        ],
    }
)
