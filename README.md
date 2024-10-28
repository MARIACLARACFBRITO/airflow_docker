# airflow_docker


# Instruções para Configuração

Siga as etapas abaixo para garantir que tudo ocorra como o esperado:

## 1. Clonar o Repositório

Abra seu terminal e execute o comando abaixo para clonar o repositório:

```bash
git clone <URL_do_repositório>
```

Claro! Aqui está um passo a passo completo para acessar e rodar o container do seu repositório no GitHub, incluindo a visualização dos arquivos no MongoDB:

markdown
Copiar código
# Passo a Passo para Acessar e Rodar o Container

Siga as etapas abaixo para clonar o repositório, construir e executar o container, e visualizar os dados no MongoDB.

## 1. Clonar o Repositório

Abra seu terminal e execute o comando abaixo para clonar o repositório:

```bash
git clone <URL_do_repositório>
```
Substitua <URL_do_repositório> pela URL do seu repositório no GitHub.

2. Navegar até o Diretório do Repositório
Entre na pasta do repositório clonado:
```
cd <nome_do_repositório>
```

  **Construir os containers do Docker:**
   ```bash
   docker-compose build
   ```
Iniciar os containers em segundo plano:

```
docker-compose up -d
```
Acessar a aplicação no navegador:

URL: http://localhost:8080

Login: airflow

Senha: airflow

Ativar a DAG e apertar o play para rodar.

Acessar o MongoDB dentro do container:
```
docker exec -it <nome_do_container> mongosh
```

Selecionar o banco de dados:

```
use banco_fiap
```

Mostrar as coleções disponíveis:

```
show collections
```

Consultar os dados na coleção info_cliente:

```
db.info_cliente.find()
```


### Dicas:
- Substitua `<nome_do_container>` pelo nome real do seu container.
- Certifique-se de que o `docker-compose` esteja instalado e configurado corretamente antes de executar os comandos.


