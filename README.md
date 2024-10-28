# airflow_docker

markdown
Copiar código
# Instruções para Configuração

Siga as etapas abaixo para garantir que tudo ocorra como o esperado:

1. **Construir os containers do Docker:**
   ```bash
   docker-compose build
Iniciar os containers em segundo plano:

'''bash
docker-compose up -d

Acessar a aplicação no navegador:

URL: http://localhost:8080
Login: airflow
Senha: airflow
Ativar a DAG e apertar o play para rodar.

Acessar o MongoDB dentro do container:

'''bash
docker exec -it <nome_do_container> mongosh

Selecionar o banco de dados:

'''bash
use banco_fiap

Mostrar as coleções disponíveis:

'''bash
show collections

Consultar os dados na coleção info_cliente:

'''bash
db.info_cliente.find()

Os dados do arquivo CSV carregados no Mongo serão exibidos.

markdown


### Dicas:
- Substitua `<nome_do_container>` pelo nome real do seu container.
- Certifique-se de que o `docker-compose` esteja instalado e configurado corretamente antes de executar os comandos.


