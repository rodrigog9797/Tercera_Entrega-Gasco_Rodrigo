from django.contrib import admin
from django.urls import path, include
from AppGasco import views, views_clases
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', views.inicio, name = "inicio"),
    path('categoria/', views.categoria, name = "categoria"),
    path('producto/', views.producto, name = "producto"),
    path('cliente/', views.cliente, name = "cliente"),
    path('categoriaFormulario/', views.categoriaFormulario, name = "CategoriaFormulario"),
    path('busqueda_DescripcionCategoria/', views.busqueda_DescripcionCategoria, name = "Busqueda_DescripcionCategoria"),
    path('AppGasco/buscar_categoria/', views.buscar_categoria, name="buscar_categoria"),
    path('clienteFormulario/', views.clienteFormulario, name = "ClienteFormulario"),
    path('busqueda_NombreCliente/', views.busqueda_NombreCliente, name = "Busqueda_NombreCliente"),
    path('AppGasco/buscar_cliente/', views.buscar_cliente, name="buscar_cliente"),
    path('productoFormulario/', views.productoFormulario, name = "ProductoFormulario"),
    path('busqueda_NombreProducto/', views.busqueda_NombreProducto, name = "Busqueda_NombreProducto"),
    path('AppGasco/buscar_producto/', views.buscar_producto, name="buscar_producto"),

]   

urls_vistas_clases_categoria = [
    path('categoria/lista/', views_clases.CategoriaListView.as_view(), name='List_Categoria'),
    path('categoria/detalle/<int:pk>/', views_clases.CategoriaDetalle.as_view(), name='Detail_Categoria'),
    path('categoria/nuevo/', views_clases.CategoriaCreateView.as_view(), name='New_Categoria'),
    path('categoria/editar/<int:pk>', views_clases.CategoriaUpdateView.as_view(), name='Edit_Categoria'),
    path('categoria/eliminar/<int:pk>', views_clases.CategoriaDeleteView.as_view(), name='Delete_Categoria')
]


urls_vistas_clases_producto = [
    path('producto/lista/', views_clases.ProductoListView.as_view(), name='List_Producto'),
    path('producto/detalle/<int:pk>/', views_clases.ProductoDetalle.as_view(), name='Detail_Producto'),
    path('producto/nuevo/', views_clases.ProductoCreateView.as_view(), name='New_Producto'),
    path('producto/editar/<int:pk>', views_clases.ProductoUpdateView.as_view(), name='Edit_Producto'),
    path('producto/eliminar/<int:pk>', views_clases.ProductoDeleteView.as_view(), name='Delete_Producto')
]

urls_vistas_clases_cliente = [
    path('cliente/lista/', views_clases.ClienteListView.as_view(), name='List_Cliente'),
    path('cliente/detalle/<int:pk>/', views_clases.ClienteDetalle.as_view(), name='Detail_Cliente'),
    path('cliente/nuevo/', views_clases.ClienteCreateView.as_view(), name='New_Cliente'),
    path('cliente/editar/<int:pk>', views_clases.ClienteUpdateView.as_view(), name='Edit_Cliente'),
    path('cliente/eliminar/<int:pk>', views_clases.ClienteDeleteView.as_view(), name='Delete_Cliente')
]

urlpatterns += urls_vistas_clases_categoria + urls_vistas_clases_producto + urls_vistas_clases_cliente