# Trabalho (Integração e Entrega contínua CI-CD)

**Equipe:** Luciano Pereira Targino, Samuel Porto, Raylson Brauna, Felipe Holanda
  
1- **Execultar o comando abaixo para adicionar o usuario Admin airflow:**

    docker exec -it <id  do  container  [sheduller-1]> airflow users create --username admin3 --firstname Admin --lastname Admin --role Admin --email admin3@email.com

2- **Depois que rodar o airflow init do banco comando:**

    docker exec -it <id  do  container  [sheduller-1]> airflow db init

**Obs:** Se ao execultar os 3 containers ocorrer erro de versão airflow:
1- Alterar no docker-compose.yml o sheduller:

    scheduler: 
	    image: apache/airflow:2.7.0 			         
	    depends_on: 
		    - webserver 
		environment: 
		    - AIRFLOW__CORE__SQL_ALCHEMY_CONN=postgresql+psycopg2://airflow:airflow@postgres/airflow
    
		    - AIRFLOW__CORE__FERNET_KEY=mhmz4vto8z6yssAV5PC6xdOOjtZMbBLU76vWMRDIpIc=
    
		    - AIRFLOW__CORE__EXECUTOR=LocalExecutor
		command: airflow db upgrade; scheduler
	    volumes:
		    - ./dags:/opt/airflow/dags

  

2- **Execultar novamente comando:**

    docker-compose up -d