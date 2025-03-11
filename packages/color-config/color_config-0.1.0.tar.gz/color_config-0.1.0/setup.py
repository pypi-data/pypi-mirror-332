from setuptools import setup, find_packages

setup(
    name="color_config",
    version="0.1.0",
    packages=find_packages(),
    install_requires=["colorama"],
    author="Dein Name",
    author_email="deine.email@example.com",
    description="Ein einfaches Farb-Config-Modul für CLI-Programme.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/deinusername/color_config",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
