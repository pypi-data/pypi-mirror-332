from setuptools import setup, find_packages

setup(
    name="muxi-ai",
    version="0.0.1",
    author="Ran Aroussi",
    author_email="ran@automaze.io",
    description="An extensible framework for building AI agents (WIP)",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/ranaroussi/muxi",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    python_requires='>=3.7',
)
