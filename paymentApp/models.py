# Importamos el módulo de modelos de Django
from django.db import models

# Creamos un modelo llamado 'Order' que hereda de 'models.Model'
class Order(models.Model):
    pass
    # En este modelo no hay campos definidos aún, pero puedes agregarlos según tus necesidades
    # Puedes añadir campos como CharField, IntegerField, DateTimeField, etc.

    # Por ejemplo:
    # nombre = models.CharField(max_length=255)
    # cantidad = models.IntegerField()
    # fecha_creacion = models.DateTimeField(auto_now_add=True)

    # Si no tienes ningún campo específico por ahora, puedes dejar el modelo vacío o agregar campos según sea necesario.

    # Nota: Un modelo en Django representa una tabla en la base de datos. Cada campo del modelo se convierte en una columna en esa tabla.
    # Los modelos te permiten definir la estructura de tus datos y cómo interactuar con ellos en tu aplicación web.
