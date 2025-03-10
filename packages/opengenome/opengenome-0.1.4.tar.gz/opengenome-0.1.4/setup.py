from setuptools import setup, find_namespace_packages, find_packages

with open('README.md', 'r') as f:
    description = f.read()

setup(
    name='opengenome',
    version='0.1.4',
    long_description=description,
    long_description_content_type="text/markdown",
    packages=find_namespace_packages(
        where="src",
        include=['opengenome', 'opengenome.*'],
        exclude=[],
    ),
    package_data={"": ["*.txt"]},
    license_files=('LICENSE.txt', ),
    package_dir={'': 'src'},
    python_requires=">=3.10",
    install_requires=[
        "torch>=2",
        "matplotlib>=3",
        "torchinfo>=1.8",
    ],
    include_package_data=True,
    entry_points={
        "console_scripts": [
            "opengenome-about = opengenome:about",
        ],
    },
    extras_require={
        "dev": [
            "mypy",
            "pytest",
            "pytest-cov",
            "jupyter",
            "sphinx",
            "myst-nb",
            "sphinx-autoapi",
            "pydata_sphinx_theme",
        ]
    },
    url="https://opengenome.readthedocs.io/en/latest/",
    project_urls={
        "Source": "https://github.com/luhouyang/opengenome",
    },
)
