Tercera Entrega del curso de Python realizada por Rodrigo Gasco

Este proyecto tiene como objetivo final realizar una aplicación web en la cual se pueda realizar compras de todo tipo de productos tecnológicos. Como por ejemplo: Teclados, telefonos, monitores, televisores, heladeras, etc.

Por el momento la aplicación incluye una pagina de inicio, en la cual se encuentran los links a cada una de las clases del proyecto:
- Categoria
- Producto
- Cliente

Estos links aún no realizan nada en especifico, simplemente toman como herencia el html de index.html, para que de esta forma se pueda visualizar lo mismo tanto en la pagina de inicio, como en cada uno de estos tres links. Teniendo como única diferencia lo escrito en el código 
    {% block contenidoQueCambia  %}
    "PARTICULARIDAD DE CADA LINK"
    {% endblock %}

Las funcionalidades de la aplicación por el momento son las siguientes:

- Agregar:
  .Productos
  .Clientes
  .Categorias

-Buscar:
  .Productos
  .Clientes
  .Categorias

A continuación voy a dejar los Productos, Clientes y Categorias agregadas para que puedan utilizar de forma practica la función de "Buscar". En todos estos casos dejare solo el elemento que se requiere para realizar la busqueda.

Clientes:
  nombre_cliente: Rodrigo        nombre_cliente: Juancito

Productos
  nombre_producto: Samsung Galaxy S24 Ultra        nombre_producto: Samsung HQ 500        nombre_producto: Iphone 16 PRO MAX

Categorias: nombre_categoria: Telefonos          nombre_categoria: Monitores          nombre_categoria: Televisores          nombre_categoria: Teclados          nombre_categoria: Mouses

Para acceder a las distintas urls, a continuación dejo los links de las mismas
  Página principal al levantar el servidor: http://127.0.0.1:8000/
  Agregar nueva categoria: http://127.0.0.1:8000/categoriaFormulario/
  Agregar nuevo producto: http://127.0.0.1:8000/productoFormulario/
  Agregar nuevo cliente: http://127.0.0.1:8000/clienteFormulario/

  Buscar categoria: http://127.0.0.1:8000/busqueda_DescripcionCategoria/
  Buscar producto: http://127.0.0.1:8000/busqueda_NombreProducto/
  Buscar cliente: http://127.0.0.1:8000/busqueda_NombreCliente/

Para acceder a la pagina de inicio: http://127.0.0.1:8000/inicio/
Para acceder a la pagina de Categoria: http://127.0.0.1:8000/categoria/
Para acceder a la pagina de Cliente: http://127.0.0.1:8000/cliente/
Para acceder a la pagina de Producto: http://127.0.0.1:8000/producto/
  
Actualmente la página sigue en construcción.
