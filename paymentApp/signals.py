# Importaciones necesarias
from django.dispatch import receiver
from paypal.standard.models import ST_PP_COMPLETED
from paypal.standard.ipn.signals import valid_ipn_received, invalid_ipn_received

# Importar el modelo Order definido en el mismo directorio
from .models import Order

# Decorador para manejar señales de IPN (pago instantáneo)
@receiver(valid_ipn_received)
def valid_ipn_signal(sender, **kwargs):
    # Imprimir mensaje para depuración
    print('ipn valid')

    # Obtener la instancia de la señal IPN
    ipn = sender

    # Verificar si el estado de pago es 'Completed' (Completado)
    if ipn.payment_status == 'Completed':
        # Realizar acciones adicionales, si es necesario

        # Crear una nueva instancia del modelo Order
        Order.objects.create()

# Decorador para manejar señales de IPN no válidas
@receiver(invalid_ipn_received)
def invalid_ipn_signal(sender, **kwargs):
    # Imprimir mensaje para depuración
    print('ipn invalid')

    # Obtener la instancia de la señal IPN
    ipn = sender

    # Verificar si el estado de pago es 'Completed' (Completado)
    if ipn.payment_status == 'Completed':
        # Realizar acciones adicionales, si es necesario

        # Crear una nueva instancia del modelo Order
        Order.objects.create()

