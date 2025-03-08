from setuptools import setup, find_packages

setup(
    name="ProxySuite",  # Your package name
    version="1.0.0",  # Version of your package
    author="chef_lilou",  # Your name or username
    author_email="georgang123@gmail.com",  # A valid email address (replace with your email)
    description="A powerful tool to scrape, check, and manage proxies.",  # Short description
    long_description=open("README.md").read(),  # Long description from README.md
    long_description_content_type="text/markdown",  # Specify the content type of the long description
    url="https://github.com/NotAdl22/ProxySuite",  # URL to your project's repository
    packages=find_packages(),  # Automatically find packages in your project
    install_requires=[  # List of dependencies
        "requests",
        "colorama",
    ],
    entry_points={  # Define command-line scripts
        "console_scripts": [
            "proxysuite=ProxySuite.main:main",  # Command: proxysuite
        ],
    },
    classifiers=[  # Metadata for PyPI
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",  # Minimum Python version required
)