# Descripción del Proyecto
# SDK de Mercado Pago para Python
# PyPI Descargas de PyPI APM

# Esta biblioteca proporciona a los desarrolladores un conjunto sencillo de enlaces
# para ayudarte a integrar la API de Mercado Pago en un sitio web y comenzar a recibir pagos.

# 💡 Requisitos
# Python 3 o superior.

# 📲 Instalación
# Ejecuta pip3 install mercadopago

# 🌟 Primeros Pasos
# ¿Es la primera vez que usas Mercado Pago? Crea tu cuenta de Mercado Pago.
# Copia tu Access Token desde el panel de credenciales y reemplaza el texto YOUR_ACCESS_TOKEN con él.

# Uso Sencillo
import mercadopago

sdk = mercadopago.SDK("YOUR_ACCESS_TOKEN")

datos_pago = {
    "transaction_amount": 100,
    "token": "CARD_TOKEN",
    "description": "Descripción del pago",
    "payment_method_id": 'visa',
    "installments": 1,
    "payer": {
        "email": 'test_user_123456@testuser.com'
    }
}
resultado = sdk.payment().create(datos_pago)
pago = resultado["response"]

print(pago)

# Configuración por solicitud
# Todos los métodos que realizan llamadas a la API aceptan un objeto RequestOptions opcional.
# Esto se puede utilizar para configurar algunas opciones especiales de la solicitud, como cambiar credenciales o encabezados personalizados.

import mercadopago
from mercadopago.config import RequestOptions

opciones_solicitud = RequestOptions(access_token='YOUR_ACCESS_TOKEN')
# ...

resultado = sdk.payment().create(datos_pago, opciones_solicitud)
pago = resultado["response"]

# 📚 Documentación
# Visita nuestro sitio para desarrolladores para obtener más información sobre:

# APIs
# Checkout Pro
# API de Checkout
# Web Tokenize Checkout
# Consulta nuestra referencia de código oficial para explorar todas las funcionalidades disponibles.

# 🤝 Contribuciones
# Todas las contribuciones son bienvenidas, desde personas que desean clasificar problemas,
# otros que desean escribir documentación, hasta personas que desean contribuir con código.

# Por favor, lee y sigue nuestras pautas de contribución. Las contribuciones que no sigan estas
# pautas serán ignoradas. Las pautas están en su lugar para facilitar nuestras vidas a todos
# y hacer que la contribución sea un proceso consistente para todos.

# ❤️ Soporte
# Si necesitas soporte técnico, por favor, contacta a nuestro equipo de soporte en developers.mercadopago.com.

# 🏻 Licencia
# Licencia MIT. Derechos de autor (c) 2021 - Mercado Pago / Mercado Libre
# Para obtener más información, consulta el archivo LICENSE.
