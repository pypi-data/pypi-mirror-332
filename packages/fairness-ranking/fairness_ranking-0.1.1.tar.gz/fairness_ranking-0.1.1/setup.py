from setuptools import setup, find_packages

# Read the README file for the long description
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="fairness_ranking",  # Your package name
    version="0.1.1",  
    author="Mallak Alkhathlan",
    author_email="malkhathlan@wpi.edu",
    description="A package for generating synthetic data, reranking students, and calculating fairness metrics.",
    long_description=long_description,
    long_description_content_type="text/markdown",  
    packages=find_packages(),
    install_requires=[
        "pandas",
        "numpy",
        "scikit-learn"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
