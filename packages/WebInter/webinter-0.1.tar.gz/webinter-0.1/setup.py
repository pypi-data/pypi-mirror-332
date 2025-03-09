from setuptools import setup, find_packages

setup(
    name='WebInter',
    version='0.1',
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'webinter = webinter.__main__:main',
        ],
    },
    description='A fast and minimalistic Python web framework with no external dependencies',
    author='Jason Schmitz',
)
