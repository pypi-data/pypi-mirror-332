import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="sdfgsdfgsdfgsdfgsdfgsehdfghjdfg",                   # Название пакета на PyPI
    version="0.0.1",                 # Версия
    author="Ваше Имя",
    author_email="youremail@example.com",
    description="Пример публикации на PyPI (без pyproject.toml)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License", 
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
