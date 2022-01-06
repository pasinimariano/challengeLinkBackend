La api fue desarollada utilizando un entorno virtual. Por lo que comenzaremos instalando dicho entorno.
El primer paso será utilizar el comando:
"pip install virtualenv" -Windows.
"apt install python3.8-venv" -Linux

Ahora que ya tenemos las dependencias necesarias, abrimos una terminal y nos ubicamos en la carpeta de nuestro proyecto:
"python -m venv env"
Esto creará nuestro entorno virtual. Como podrás ver aparecerá un nuevo directorio en el proyecto, llamado "env". Eso indica
que vamos por buen camino.

Para activarlo y poder comenzar a trabajar.
"source env/bin/activate".
Debería aparecer delante del nombre del proyecto -> (env), eso indica que estás trabajando en un entorno virtual.

Con el entorno activado, en la terminal ejecutamos el comando:
"pip install -r requirements.txt"
Esto instalará todas las dependencias necesarias utilizadas en el proyecto.
Lo bueno del entorno virtual es que todas estas dependencias no se instalarán a nivel global en tu equipo, sino que por el
contrario se instalarán dentro de "env/lib".
Esto quiere decir que siempre que quieras utilizar el proyecto deberás activar el entorno, con el comando anteriormente
mencionado.

El último paso a realizar será crear un nuevo archivo llamado ".env", donde se almacenarán todas las variables de entorno.
Por el momento necesitamos tener:
SECRET_KEY=my_secret_key
PORT=my_port

Con todos estos requisitos cumplidos la api funcionará correctamente.
Para correr el proyecto, en una terminal, dentro del entorno virtual, utilizaremos el comando:
"python src/app.py".

Si en algún momento quieres salir del entorno virtual, basta con colocar "deactivate".
