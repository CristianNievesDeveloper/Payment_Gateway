"""
URL configuration for django_payment project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# Importamos las funciones y clases necesarias de Django
from django.contrib import admin
from django.urls import path, include
from paymentApp import views  # Importamos las vistas de nuestra aplicación paymentApp


# Definimos las URL de nuestra aplicación
urlpatterns = [
    # URL para acceder a la interfaz de administración de Django
    path('admin/', admin.site.urls),
    
    # URL para manejar las notificaciones de PayPal mediante la aplicación django-paypal
    # Incluimos las URLs proporcionadas por la aplicación django-paypal
    path('paypal/', include('paypal.standard.ipn.urls')),
    
    # URL principal de nuestra aplicación, incluimos las URLs definidas en paymentApp.urls
    path('live/', include('paymentApp.urls')),
    
    path('accounts/', include('allauth.urls')),

    path('', include('loginApp.urls')),

]

