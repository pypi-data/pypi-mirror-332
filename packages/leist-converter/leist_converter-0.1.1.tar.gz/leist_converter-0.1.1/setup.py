from setuptools import setup, find_packages

setup(
    name="leist_converter",
    version="0.1.1",
    packages=find_packages(),
    install_requires=[],
    author="Jonah Wendel",
    author_email="",
    description="Ein Python-Modul, das modernen Text in altdeutsche Schreibweise umwandelt",
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/w-jonah/leist_converter.git",
    classifiers=[  # Wichtige Metadaten für PyPI
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',  # Mindest-Python-Version
)
