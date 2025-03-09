from setuptools import setup, find_packages

setup(
    name="easy-transformers-finetune",  # Name of the package
    version="0.1.0",  # Version number
    description="A simple library for fine-tuning transformer models for various NLP tasks.",
    long_description=open('README.md').read(),  # Long description from README
    long_description_content_type="text/markdown",  # Specify the markdown type
    author="Your Name",
    author_email="your.email@example.com",
    url="https://github.com/yourusername/easy-transformers-finetune",  # Project URL
    packages=find_packages(),  # Automatically find and include all packages
    install_requires=[
        'transformers>=4.0.0',
        'torch>=1.7.0',
        'datasets>=1.0.0',
        'scikit-learn>=0.24.0'
    ],  # List of dependencies
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',  # Supported Python versions
)
