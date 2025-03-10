from setuptools import setup, find_packages

setup(
    name="urlF",  # Package name
    version="2.0",  # Update this version as needed
    author="0xBobby",
    author_email="rule-entry-0d@icloud.com",  # Replace with your email
    description="A tool to filter and deduplicate URLs based on domain and query parameters.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Boopath1/urlF",  # Replace with your repo
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "art",
        "colorlog",
        "tqdm",
        "colorama"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    entry_points={
        "console_scripts": [
            "urlf=urlf.urlf:main",
        ],
    },
)