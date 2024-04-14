# Entrar a contenedor
1. Primero encontrar el id del contenedor
docker ps
2. Una vez encontrado el id
docker exec -it <id> bash



#Visualizar tablas y bbdd de mysql
1. Entrar al contenedor:
docker exec -it <id> bash
2. usando el client mysql logearse
mysql -u root -p
Password: patata definida como variable de entorno en docker-compse
3. Listar los databases:
show databases;
4. Selecionar un database:
use Asignatura;
5. Listar las tablas:
show tables;
6. Ver esquema de tabla;
describe Clase;
