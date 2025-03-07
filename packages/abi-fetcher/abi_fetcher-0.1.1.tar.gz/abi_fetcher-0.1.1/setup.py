from setuptools import setup, find_packages

setup(
    name="abi-fetcher",
    version="0.1.01",
    packages=find_packages(),
    install_requires=["requests"
    ],
    entry_points={
        "console_scripts": [
            "abi-fetcher=abi_fetcher.client:main",  # Optional CLI
        ],
    },
    author="Yann Neve",
    package_data={
        # Include the JSON file inside the package
        'abi_fetcher': ['chainlist.json', 'README.md']},
    author_email="yann.nx321.subprime216@simplelogin.com",
    description="A Python package to fetch smart contract ABIs from all EVM compatible blockchains",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/zorglob21/ABI_fetcher",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)

