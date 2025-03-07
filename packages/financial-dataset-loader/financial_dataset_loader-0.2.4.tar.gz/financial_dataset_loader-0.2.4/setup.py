from setuptools import setup, find_packages

setup(
    name='financial_dataset_loader',
    version='0.2.4',
    packages=find_packages(),
    install_requires=[
        'aws-s3-controller',
        'string-date-controller',
        'shining_pebbles',
    ],
    author='June Young Park',
    author_email='juneyoungpaak@gmail.com',
    description='A Python module for loading financial datasets from various sources',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/nailen1/financial_dataset_loader.git',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Financial and Insurance Industry',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Office/Business :: Financial',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.11',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.11',
    keywords='financial data loader dataset aws s3',
)
