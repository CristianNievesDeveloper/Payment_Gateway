# Este archivo (urls.py) define las URL (rutas) de la aplicación 'paymentApp' en Django.

# Importa la función 'path' del módulo 'django.urls' y las vistas definidas en el archivo 'views.py'.
from django.urls import path
from . import views



# Lista de patrones de URL para la aplicación 'paymentApp'.
urlpatterns = [
    # Ruta para la vista 'payment', sin un segmento específico en la URL.
    # Cuando un usuario accede a la raíz del sitio, se dirigirá a la vista 'payment'.
    path('', views.payment, name='payment'),

    # Ruta para la vista 'paypal_return', accesible a través de '/paypal-return'.
    # Se utiliza para manejar el retorno de PayPal después de una transacción exitosa.
    path('paypal-return', views.paypal_return, name='paypal-return'),

    # Ruta para la vista 'paypal_cancel', accesible a través de '/paypal-cancel'.
    # Se utiliza para manejar la cancelación de una transacción de PayPal.
    path('paypal-cancel', views.paypal_cancel, name='paypal-cancel'),
    
]




