from setuptools import setup, find_packages

setup(
    name='runex',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[],
    description='A helper to manage ML experiments.',
    entry_points={
        'console_scripts': [
            'runex=runex:cli',
        ],
    },
)