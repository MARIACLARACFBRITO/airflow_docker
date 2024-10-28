# airflow_docker

Vamos ajustar para que todos os comandos fiquem formatados corretamente. Aqui está a versão revisada:

markdown
Copiar código
# Instruções para Configuração

Siga as etapas abaixo para garantir que tudo ocorra como o esperado:

 1. **Construir os containers do Docker:**
   ```bash
   docker-compose build
   
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


