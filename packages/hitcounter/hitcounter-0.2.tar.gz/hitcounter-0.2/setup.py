from setuptools import setup, find_packages

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='hitcounter',
    version='0.2',
    description='A simple AWS CDK construct for counting hits',
    author='MigHerm',
    author_email='miguelangel.hermar410@gmail.com',
    packages=find_packages(),
    install_requires=[
        'aws-cdk-lib',
        'constructs'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.10',
    ],
    long_description=long_description,
    long_description_content_type='text/markdown'
)