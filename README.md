# Sistema de Gestão de Cursos

## Descrição do Projeto

## Requisitos

- **Python 3.13** – Linguagem de programação base do projeto.
- **UV** - Gerenciador de ambiente e dependências.
- **Django** – Framework web principal, utilizado para construir a aplicação e suas funcionalidades.
- **Docker** - Utilizado para subir e gerenciar o contêiner do banco de dados PostgreSQL

## Como Instalar e Rodar o Projeto Localmente

Siga os passos abaixo para configurar o ambiente e executar o projeto em sua máquina local:

### 1. Clone o repositório do GitHub:

Abra um terminal e rode:
```bash
git clone https://github.com/robsonlopesjr/gestao-de-cursos
```

Em seguida, navegue até o diretório do projeto:
```bash
cd gestao-de-cursos
```

### 2. Instale as dependências do projeto:

<em><b>Atenção</b>: Foi utilizado o <b>uv</b> para controle de dependências, caso não tenha o mesmo instalado você pode estar executando o comando:</em>

```bash
pip install uv
```

Instalando as dependências:
```bash
uv sync
```

### Configuração do Banco de Dados

Nesse projeto foi utilizado o Banco de Dados Postgres com a imagem gerado via Docker em `infra/composer.yaml` e as credenciais de acesso estão em `.env.development`.

Para subir a imagem do Banco de Dados Postgres:
```bash
docker compose -f infra/compose.yaml up -d
```

Para encerrar a imagem do Banco de Dados Postgres:
```bash
docker compose -f infra/compose.yaml down
```

Mas caso opte por outras configurações de Banco de Dados você pode estar alterando o arquivo `app/settings.py`:
```python
DATABASES = {
    "default": {
        "ENGINE": os.environ.get("DATABASE_ENGINE"),
        "NAME": os.environ.get("POSTGRES_DB"),
        "USER": os.environ.get("POSTGRES_USER"),
        "PASSWORD": os.environ.get("POSTGRES_PASSWORD"),
        "HOST": os.environ.get("POSTGRES_HOST"),
        "PORT": os.environ.get("POSTGRES_PORT"),
    }
}
```

### Executa as migration para criar as tabelas.
```bash
uv run manage.py migrate
```

### Crie um super usuário.
```bash
uv run manage.py createsuperuser
```

### Execute o servidor de desenvolvimento.
```bash
uv run manage.py runserver
```

Por padrão, o servidor estará disponível em http://127.0.0.1:8000/. Você deverá ver no terminal a mensagem indicando que o servidor está rodando e acessível.