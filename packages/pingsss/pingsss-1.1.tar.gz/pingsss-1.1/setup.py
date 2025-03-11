# setup.py
from setuptools import setup

setup(
    name='pingsss',
    version='1.1',
    packages=['pingsss'],
    install_requires=['colorama','ipaddress'],
    entry_points={
        'console_scripts': [
            'pingsss = pingsss.pingsss:main',
        ],
    },
)
