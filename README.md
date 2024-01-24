# Amostra Simples de ETL

## Clonar repositório do projeto

```shell
git clone https://github.com/andersonbraz/sample-multi-pipelines.git
```

## Configurando ambiente do projeto

```shell
python -m venv .venv && . .venv/bin/activate && python -m pip install --upgrade pip
```

OU

```shell
python3 -m venv .venv && . .venv/bin/activate && python3 -m pip install --upgrade pip
```

## Instalar dependencias do projeto

```shell
pip install -r requirements.txt
```

## Criar token API com seu usuário Github

[https://github.com/settings/tokens/](https://github.com/settings/tokens/)

## Configurar variável de ambiente com token do Github

No Linux ou MacOS:

```shell
export GITHUB_TOKEN=ghp_1df69a140409ea867f9cd4060523ab9d
```

No Windows:

```ps
setx GITHUB_TOKEN ghp_1df69a140409ea867f9cd4060523ab9d
```

** Esse token é FAKE, tá? kkkk

## Executando o projeto - Github

```shell
python workflow-git.py
```

## Executando o projeto - Kabum

```shell
python workflow-github.py
```

## Referências

- [Documentação da API REST do GitHub](https://docs.github.com/pt/rest?apiVersion=2022-11-28)

- [Microsoft Edge WebDriver](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/)
