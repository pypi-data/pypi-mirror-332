from setuptools import setup, find_packages
import os

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as file:
    desc = file.read()

setup(
    name='example_package_unnamed73533',
    version='0.0.1',
    install_requires=[
        'requests',
    ],
    description='cba',
    author='unnamed7353',
    author_email='unnamed7353@gmail.com',
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3"
    ],
    packages=find_packages(),
    long_description=desc,
    long_description_content_type='text/markdown'
)