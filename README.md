<h1> Tarea 2 - Test CHR </h1>

<p>Se solicita la creacion de un script para la obtencion de información de una tabla de un sitio publico. Se debe crear un modelo y dicha información sera guardada en este modelo que aplique a la misma.</p>

<p>Para el cumplimiento de la tarea se utilizo el lenguaje Python con el framework Django, y contando con PostgreSQL como base de datos. También se hizo uso de virtualenv para la creación de un entorno virtual donde estaremos instalando las librerias necesarias.</p>

<em># Pasos a tener en cuenta para su instalación y uso</em>
<ul>
  <li>Clonar el repositorio</li>
  
  $ git clone https://github.com/Anibal-Reinoso/TAREA-2-CHR/
  
  <li>Entrar en el directorio y crear un entorno virtual</li>
  
  $ cd TAREA-2-CHR
  
  $ virtualenv venv
  
  <li>Activar el entorno virtual</li>
  
  $ source venv/bin/actvate en linux Or Unix
  
  $ call venv/Scripts/activate en Windows
  
  <li>Instalar los requerimientos</li>
  
  $ pip install -r requirements.txt
  
  <li>Ingresar a la carpeta del proyecto y correr el script</li>
  
  $ cd CHR
  
  $ python manage.py runserver
  
  Accedemos a 127.0.0.1:8000 o localhost:800 para visualizar la información
</ul>

<em># Para acceder al administrador</em>
<ul>
  <li>Ingresamos a 127.0.0.1:8000/admin o localhost:8000/admin</li>

  En este caso pondremos como usuario y password "admin"
  
  Asi podremos ver los modelos y la data dentro de cada uno.
</ul>

<<Dato a tener en cuenta: intenté recorrer las paginas del sitio pero por alguna razon no podia acceder a la tabla cuando se marcaban las demas páginas, el script funciona con la url solicitada, y puede ser modificada para el resto de las páginas, pero por motivos de tiempo no encontre forma de traer el resto de la información de la tabla.>>
