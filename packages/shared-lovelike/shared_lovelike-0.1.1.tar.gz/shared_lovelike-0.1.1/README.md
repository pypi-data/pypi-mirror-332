# shared-lovelike

Existe duas formas de usar, a segunda é mais aconselhada

1 forma:

clonar esse repositorio na raiz do projeto

cd shared_lovelike

pip install .

2 forma:

pip install git+https://github.com/LLstartup/shared_lovelike.git@development#egg=shared_lovelike


## Criando pacotes

pip install setuptools wheel twine

criar o arquivo setup.py na raiz do projeto

criar a distribuição com esse comando:

python setup.py sdist bdist_wheel


## Publicando pacotes

Para configurar suas credenciais, execute o comando:

python -m twine upload --repository-url https://upload.pypi.org/legacy/ dist/*

twine upload --repository-url https://upload.pypi.org/legacy/ dist/*





