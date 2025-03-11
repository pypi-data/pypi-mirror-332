from setuptools import setup, find_packages

setup(
    name='nlkt', 
    version='0.0.1',
    description='A Python library for building ML models and printing code.',
    author='CrypticX',
    author_email='srdeepak78@gamil.com',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'nltk',
        'pandas'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
