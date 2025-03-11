from setuptools import setup, find_packages

setup(
    name="shared_lovelike",
    version="0.1.0",
    packages=find_packages(),
    description="Pacote responsavel por compartilhar as entidades do projeto LoveLike",
    author="George Augusto da Silva",
    author_email="ge_silva1991@hotmail.com",
    install_requires=[
        "fastapi>=0.115.8",
        "SQLAlchemy>=2.0.37",
        "psycopg2>=2.9.10",
        "alembic>=1.14.1",
    ],
    # package_dir={'': 'src'},
)
