# Pasos previos
Instalar entorno virtual

x:> ```pip install virtualenv```

Crear entorno virtual

x:> ```virtualenv -p python3 env```

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

## Base de datos
Preparacion de la base de datos
```
CREATE TABLE supers (
  id_super INT(6) AUTO_INCREMENT PRIMARY KEY,
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

```
