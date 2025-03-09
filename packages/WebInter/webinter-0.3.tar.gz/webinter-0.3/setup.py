from setuptools import setup, find_packages
import os
def read_readme():
    with open(os.path.join(os.path.dirname(__file__), 'README.md'), encoding='utf-8') as f:
        return f.read()

setup(
    name='WebInter',
    version='0.3',
    packages=find_packages(),
    install_requires=[],  
    entry_points={
        'console_scripts': [
            'webinter = webinter.__main__:main', 
        ],
    },
    description='A fast and minimalistic Python web framework with no external dependencies',
    long_description=read_readme(),  
    long_description_content_type='text/markdown', 
    author='Jason Schmitz',
    author_email='support@faysi.de', 
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'License :: OSI Approved :: MIT License',  
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7', 
)
