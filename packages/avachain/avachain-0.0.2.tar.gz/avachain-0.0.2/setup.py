from setuptools import setup, find_packages
import os


# Read the README file
def read(file_name):
    return open(os.path.join(os.path.dirname(__file__), file_name)).read()


setup(
    name="avachain",
    version="0.0.2",
    packages=find_packages(),
    install_requires=[
        # "pydantic>=2.6.1",
        # "requests>=2.31.0",
        "mistralai==0.4.2",
        "anthropic",
        "semantic-text-splitter",
        "tokenizers",
        "openai",
        # "cartesia==0.1.0",
        # "pydub",
        # "numpy",
        "print_color",
        # List dependencies here
    ],
    author="Pranshu Ranjan",
    author_email="pranshuranjan@pathor.in",
    maintainer="Salo Soja Edwin",
    maintainer_email="salosoja@pathor.in",
    description="A very light weight library to create and run agent with tools, with any LLM supported openai spec, Claude, Mistral.",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    license="MIT",
    # url='https://github.com/your_username/your_package_name',
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
)
