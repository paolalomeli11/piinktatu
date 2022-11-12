ANTES QUE NADA ES DE SUMA IMPORTANCIA INSTALAR LA VERSIÓN MÁS RECINETE PYTHON JUNTO CON SU INTERPRETE PARA PODER TRABAJAR CON
EL FRAMEWORK DJANGO

1- Instalar Python
	
	- Visita el sitio oficial de python para descargar el interprete. (https://www.python.org/)
	- En la sección de 'Downloads' podrás encontrar la versión más reciente para tu sistema operativo.
	- Una vez descargado el archivo .exe (en el caso de Windows), ejecutamos como administrador para
	iniciar con el instalador, en la primera ventana, es ESENCIAL marcar la opción de 'Agregar Python
	al path', ya que sin está opción, el sistema operativo no podrá reconocer los comandos que inicien
	con python en la terminal.
	
	-Para comprobar la instalción correctamente, podemos ingresar en la terminal de Windows el comando
	'python -V', este comando arrojara la versión instalada en el SO.

2 - Instalar PIP (el manejador de paquetes de python es necesario para poder instalar el framework django)
	
	- La manera más fácil de instalar PIP basta con solo abrir la terminal en windows y agregar el comando
	'curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py'. Una vez terminado esto, proceden a ingresar
	el comando 'python get-pip.py'.
	
	- Para comprobar la instalación, nos dirigimos a la terminal e ingresamos al comando 'pip -V',
	este comando arroja la versión instalada.


3 - Instalar el framework Django
	
	- Una vez instalado pip, procedemos a instalar el framework. Basta con solo abrir la terminal
	y ejecutar el siguiente comando 'python -m pip install Django', al finalizar la descarga, ingresamos
	el comando 'python' para comenzar con el interprete de python, ya dentro ingresamos la línea
	'import django' para importar el modulo del framework, en caso de que no tire ningún error, eso
	quiere decir que no hubo ningún problema con la instalación.



Para poder correr cualquier proyecto de Django, es necesario abrir la terminal, y cambiar el directorio
a la carpeta padre del proyecto, una vez dentro, ingresamos el comando 'python manage.py runserver' para
poder correr el servidor local y pueda ser posible visualizar el proyecto. (Sin mencionar los errores que
puedan ocurrir por las configuraciones de las bases de datos, como las contraseñas y los usuarios)
	
	
