Entrega final del curso de Python de CoderHouse - Rodrigo Gasco Hernandez

Descripción del proyecto:
Este proyecto consiste en una aplicación web en la cual se pueden visualizar todas las categorias disponibles en la pagina, asi como los productos que tiene disponibles. Además tiene un registro de usuario e inicio de sesión, los cuales te permiten aceder a apartados de la pagina como Clientes(Solo usuario administrador), crear, ver, editar y eliminar(eliminar solo para el usuario administrador) tanto categorias como productos de la misma y clientes para el caso del adminisrador.

Usuarios con los permisos correspondientes:
- Usuario Administrador
  User: Rodrigo97
  Pass: T108779q!

- Usuarios comunes

 User: Usuario1
 Pass: T108779q!

 User: Usuario2
 Pass: T108779q!

 User: Usuario3
 Pass: T108779q!

Al levantar la página web desde la terminal: python manage.py runserver (Asegurarse de estar en la ruta correcta)
Directamente nos dirige al inicio de la pagina, sin la necesidad de ingresar manualmente con /inicio por ejemplo.
Link principal: http://127.0.0.1:8000/

La pagina principal contiene dintintos botones en la barra de navegación que te permiten realizar todas las funcionalidades de la misma, sin la necesidad de ingresar a rutas que no esten a simple vista o con el alcance de un botón.
- Los botones de la barra de navegación son los siguientes:
  Tecnologias Gasco: redirige a la pagina de inicio
  Inicio: también redirige a la pagina de inicio
  Categoria: redirige a un apartado visual donde se muestran algunas categorias con imagenes y nos permite con un boton acceder a "Ver Categorias"
  Producto: redirige a un apartado visual donde se muestran algunos productos con imagenes y nos permite con un boton acceder a "Ver Productos"
  Ver Categorias: redigirige a una vista en la cual podemos visualizar todas las categorias creadas. El usuario administrador podra ver, editar, elimiar, crear y buscar categorias. Los usuarios comunes podran hacer todo esto menos eliminar categorias y aquellos que no inicien sesión solo podran visualizar lo que hay en el link "Ver categorias" y podran realizar busquedas de las mismas
  Ver Productos: tiene las mismas funcionalidades que el apartado de arriba pero para los productos
  Ver Clientes: a este apartado solo puede ingresar el usuario administrador, el cual podrá visualizar, editar, eliminar, buscar o crear nuevos clientes
  Iniciar sesión: te redirige al inicio de sesión, una vez inicies la sesión en su lugar aparecera un texto que indique "Bienvenido y el user del usuario", además apareceran dos botones más al costado, uno que te permitirá editar el usuario (Nombre, Apellido, Correo y su contraseña), y el otro botón te permitirá cerrar la sesión
  Registrarse: te redirige a un formulario que te permitirá realizar la creación de un usuario, el cual debe obtener posteriormente los permisos del administrador para que pueda hacer uso de los permisos de Usuario común para mayor seguridad

  Para poder hacer uso correspondiente de la aplicación sin tener ningún inconveniente, asgurate de clonar este repositorio en tu computadora, para ello puedes usar el siguiente comando en tu terminal:
  git clone "link del repositorio que deseas clonar"

  Además asegurate de crear un entorno virtual e instalar todo lo que contenga el archivo requirements.txt


