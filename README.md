# Pasos previos
Instalar entorno virtual

x:> ```pip install virtualenv```

Crear entorno virtual en win 10

x:> ```virtualenv -p python3 env```

Crear entorno virtual en win11

x:> ``` python -m venv env```

Permisos de ejecucion con power shell

PS x:> ```Set-ExecutionPolicy RemoteSigned -Scope CurrentUser```

Entrar en el entorno virtual

x:> ```.\env\Scripts\activate```

Listar pip

(env) PS x:> ```pip list```

Instalar flask

(env) PS x:> ```pip install flask```

Instalar mysql

(env) PS x:> ```pip install flask_mysqldb```

(env) PS x:> ```pip list```

Iniciar aplicacion

(env) PS x:> ```python ./app/app.py```

## Base de datos
Preparacion de la base de datos
```
CREATE TABLE supers (
  id_super INT(2) AUTO_INCREMENT PRIMARY KEY,
  nom_super CHAR(16)
);

INSERT INTO supers (id_super, nom_super) VALUES
  (1, 'Carrefour'),
  (2, 'Mercadona'),
  (3, 'Alcampo'),
  (4, 'Eroski');

CREATE TABLE users (
  id_user INT(6) AUTO_INCREMENT PRIMARY KEY,
  username VARCHAR(20),
  nom_user VARCHAR(50),
  password CHAR(120)
);

CREATE TABLE productos (
	id_producto INT(2) AUTO_INCREMENT PRIMARY KEY,
	nombre_producto CHAR(20),
	cantidad_producto INT(2)
);

INSERT INTO productos (id_producto, nombre_producto, cantidad_producto) VALUES
  (1,'Arroz',10),
  (2,'Azucar',9),
  (3,'Harina',8),
  (4,'Fideo',5),
  (5,'Sal',5),
  (6,'Aceite',5),
  (7,'Legumbre',5),
  (8,'Leche',5),
  (9,'Cafe',5),
  (10,'Cacao',5);
```
