import uuid
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from paypal.standard.forms import PayPalPaymentsForm
from django.conf import settings


# Vista para procesar el pago
def payment(request):
    # Obtener el host de la solicitud actual
    host = request.get_host()

    # Configuración de parámetros para la integración de PayPal
    paypal_dict = {
        "business": settings.PAYPAL_RECIVER_EMAIL,  # Correo electrónico del destinatario de PayPal
        "amount": "00.01",  # Monto del pago
        "item_name": "Name Product",  # Nombre del producto o ítem
        "invoice": str(uuid.uuid4()),  # Número de factura único generado con UUID
        "currency_code" : "USD",  # Código de moneda (USD en este caso)
        "notify_url": f'http://{host}{reverse("paypal-ipn")}',  # URL de notificación de IPN
        "return_url": f'http://{host}{reverse("paypal-return")}',  # URL de retorno después del pago exitoso
        #"return": request.build_absolute_uri(reverse('your-return-view')),
        # "cancel_return": request.build_absolute_uri(reverse('your-cancel-view')),
        "cancel_return": f'http://{host}{reverse("paypal-cancel")}',  # URL de retorno después de la cancelación del pago
    }
     # Crear formulario de pago de PayPal con los parámetros configurados
    form = PayPalPaymentsForm(initial=paypal_dict)

    # Contexto para pasar al template 'payment.html'
    context = {'form': form}

    # Renderizar la plantilla 'payment.html' con el formulario de pago
    return render(request, 'payment.html', context)

# Vista de retorno después de un pago exitoso
def paypal_return(request):
    # Mostrar mensaje de éxito
    messages.success(request, 'paypal return')
    # Redirigir a la página de pago
    return redirect('payment')

# Vista de retorno después de la cancelación del pago
def paypal_cancel(request):
    # Mostrar mensaje de error
    messages.error(request, 'paypal cancel')
    # Redirigir a la página de pago
    return redirect('payment')








# def procesar_pago(request):
#     sdk = mercadopago.SDK(settings.MERCADOPAGO_ACCESS_TOKEN)

#     datos_pago = {
#         "transaction_amount": 1,
#         "token": "4509 9535 6623 3704",
#         "description": "Descripción del pago",
#         "payment_method_id": 'visa',
#         "installments": 1,
#         "payer": {
#             "email": 'test_user_123456@testuser.com'
#         }
#     }

#     resultado = sdk.payment().create(datos_pago)
#     pago = resultado["response"]

#     print(pago)

#     # Resto de la lógica de tu vista...

# # views.py


# def procesar_pago(request):
#     sdk = mercadopago.SDK(settings.MERCADOPAGO_ACCESS_TOKEN)

#     opciones_solicitud = RequestOptions(access_token=settings.MERCADOPAGO_ACCESS_TOKEN)

#     datos_pago = {
#         # ... (datos de pago)
#     }

#     resultado = sdk.payment().create(datos_pago, opciones_solicitud)
#     pago = resultado["response"]

#     # Resto de la lógica de tu vista...

