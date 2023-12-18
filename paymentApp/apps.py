# Importa la clase `AppConfig` de `django.apps`.
from django.apps import AppConfig

# Define la configuración de la aplicación `paymentApp` extendiendo la clase `AppConfig`.
class PaymentappConfig(AppConfig):
    # Configura el campo automático predeterminado para ser un campo grande (`BigAutoField`).
    default_auto_field = 'django.db.models.BigAutoField'
    
    # Establece el nombre de la aplicación como 'paymentApp'.
    name = 'paymentApp'

    # Define el método `ready`, que se llama cuando la aplicación está lista.
    def ready(self):
        # Importa el módulo de señales (`signals`) desde la aplicación `paymentApp`.
        import paymentApp.signals
