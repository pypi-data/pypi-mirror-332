from setuptools import setup, find_packages

setup(
    name="kumosense-gita",
    version="1.0.3",
    packages=find_packages(),
    install_requires=[
        "click==8.1.8",
        "GitPython==3.1.44",
        "g4f==0.4.8.0"
    ],
    entry_points={
        "console_scripts": [
            "gita=gita.cli:cli",
        ],
    },
    author="Sizning Ismingiz",
    author_email="contact@muhiddindev.uz",
    description="Gita - AI yordamida avtomatik commit yozish CLI",
    long_description=open(
        "README.md", encoding="utf-8").read(),  # UTF-8 qo'shildi
    long_description_content_type="text/markdown",
    # GitHub yoki loyiha URL'ini qo‘shing
    url="https://github.com/Muhiddin0/gita-commit",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
