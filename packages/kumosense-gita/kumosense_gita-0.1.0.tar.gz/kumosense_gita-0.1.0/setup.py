from setuptools import setup, find_packages

setup(
    name="kumosense-gita",
    version="0.1.0",
    author="Muhiddin Kabraliev",
    author_email="contact@muhiddidnev.uz",
    description="Git commitlarni avtomatlashtirish uchun AI CLI vositasi",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com//muhiddin0/gita",
    license="MIT",
    packages=find_packages(),
    install_requires=[
        "click",
        "g4f",
        "gitpython"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    entry_points={
        "console_scripts": [
            "gita=gita.cli:cli",
        ],
    },
    include_package_data=True,
)

