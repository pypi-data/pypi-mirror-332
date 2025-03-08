from setuptools import setup, find_packages

setup(
    name="nwlabchat",  # Name of your package
    version="1.0",     # Version number
    author="Hakim Adiche",
    author_email="adiche@kfupm.edu.sa",
    description="Chat program based on client/server model",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),  # Automatically finds packages in the directory
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",  # Minimum Python version required
    install_requires=[],      # List of dependencies
)
