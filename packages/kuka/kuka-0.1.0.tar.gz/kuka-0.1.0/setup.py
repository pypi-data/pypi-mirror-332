from setuptools import setup, find_packages

setup(
    name="kuka",  # Nome do pacote
    version="0.1.0",    # Versão inicial
    author="tenoriolms",
    description="Personal library for EDA, data modeling, and ML modeling analysis/interpretation",
    long_description=open("README.md").read(),  # Descrição longa
    long_description_content_type="text/markdown",  # Para suportar Markdown
    url="", # Repositório do projeto
    packages=find_packages(),  # Encontra automaticamente subpacotes
    install_requires=[
        'numpy', 
        'pandas', 
        'matplotlib'
        ],  
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",  # Versão mínima do Python
)