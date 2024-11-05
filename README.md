# airflow_docker

Setup Instructions
Follow the steps below to ensure everything works as expected:

# 1. Clone the Repository
Open your terminal and run the command below to clone the repository:

```bash
git clone https://github.com/MARIACLARACFBRITO/airflow_docker.git
```


# 2. Navigate to the Repository Directory
Enter the folder of the cloned repository:
```
cd airflow_docker/airflow

```

**Build the Docker containers:**
   ```bash
   docker-compose build
   ```
Start the containers in the background:

```
docker-compose up -d
```
Access the application in the browser:

URL: http://localhost:8080

Login: airflow

Senha: airflow

Activate the DAG and click play to run it.

Access MongoDB inside the container:
```
docker exec -it <nome_do_container> mongosh
```

Select the database:

```
use banco_fiap
```

Show the available collections:

```
show collections
```

Query the data in the info_cliente collection:

```
db.info_cliente.find()
```


### Tips:
Replace <container_name> with the actual name of your container.
Make sure that docker-compose is installed and configured correctly before running the commands.


