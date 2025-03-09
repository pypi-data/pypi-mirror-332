from setuptools import setup, find_packages

setup(
    name="RapidHost",
    version="4.0.2",
    author="Leonardo Trevisan Nery",
    author_email="leonardonery616@gmail.com",
    description="Um pacote Flask para hospedar páginas e criar rotas dinamicamente.",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/seuusuario/meu_pacote",  # Substitua pelo seu repositório
    packages=find_packages(),
    install_requires=["Flask"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
