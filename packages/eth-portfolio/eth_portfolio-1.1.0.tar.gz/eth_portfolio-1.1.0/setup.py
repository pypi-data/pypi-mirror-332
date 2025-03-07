from setuptools import find_packages, setup  # type: ignore

with open("requirements.txt", "r") as f:
    requirements = list(map(str.strip, f.read().split("\n")))[:-1]

with open("README.md", "r") as fh:
    README = fh.read()


setup(
    name="eth-portfolio",
    version="1.1.0",
    description="eth-portfolio makes it easy to analyze your portfolio.",
    author="BobTheBuidler",
    author_email="bobthebuidlerdefi@gmail.com",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/BobTheBuidler/eth-portfolio",
    project_urls={
        'Homepage': 'https://github.com/BobTheBuidler/eth-portfolio',
        'Documentation': 'https://bobthebuidler.github.io/eth-portfolio',
        'Source Code': 'https://github.com/BobTheBuidler/eth-portfolio',
    },
    packages=find_packages(),
    install_requires=requirements,
    #setup_requires=["setuptools_scm", "cython"],
    package_data={
        "eth_portfolio": ["py.typed"],
    },

)
