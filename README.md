# Generador y Verificador de Tokens JWT para App Store Connect

Este script de Python genera un token JWT (JSON Web Token) y lo utiliza para obtener información de transacciones de suscripciones desde la API de App Store Connect.

## ¿Qué hace este código?

1.  **Genera un Token JWT:**
    * Crea un token especial que sirve como "llave" para acceder a la API de Apple.
    * El token incluye información como el ID del emisor, el tiempo de creación y expiración, y el ID del paquete de la aplicación.
    * Utiliza una clave privada para firmar el token, lo que garantiza su seguridad.
2.  **Solicita Información de Transacciones:**
    * Utiliza el token generado para hacer una solicitud a la API de App Store Connect.
    * Obtiene información sobre una transacción de suscripción específica, identificada por su `TRANSACTION_ID`.
    * Decodifica los datos devueltos por la API para que sean legibles.
3.  **Muestra la información:**
    * Imprime en la pantalla el token generado, la información de la transacción, y los datos decodificados de `signedTransactionInfo` y `signedRenewalInfo`.

## ¿Cómo usarlo?

1.  **Requisitos:**
    * Asegúrate de tener Python instalado en tu computadora.
    * Necesitas las bibliotecas `jwt` y `requests`. Puedes instalarlas usando `pip install pyjwt requests`.
2.  **Configuración:**
    * Reemplaza los siguientes valores con tu información:
        * `KEY_ID`: El ID de tu clave de API de App Store Connect.
        * `ISSUER_ID`: El ID del emisor de tu cuenta de App Store Connect.
        * `BUNDLE_ID`: El ID del paquete de tu aplicación (por ejemplo, `com.tuapp`).
        * `PRIVATE_KEY_PATH`: La ruta a tu archivo de clave privada (`.p8`).
        * `TRANSACTION_ID`: El ID de la transacción que quieres consultar.
3.  **Ejecución:**
    * Guarda el código en un archivo `.py` (por ejemplo, `obtener_transaccion.py`).
    * Abre una terminal o línea de comandos y ejecuta el script con `python obtener_transaccion.py`.
4.  **Resultados:**
    * Verás el token generado, el código de respuesta de la API, y la información de la transacción en la pantalla.

## Entendiendo el código

* **JWT (JSON Web Token):** Es como un pase seguro que permite a tu aplicación acceder a la API de Apple.
* **Clave Privada:** Es un archivo secreto que se utiliza para firmar el token y hacerlo seguro.
* **API de App Store Connect:** Es el servicio de Apple que te permite acceder a información sobre tus aplicaciones y suscripciones.
* **`signedTransactionInfo` y `signedRenewalInfo`:** Contienen información detallada sobre la transacción y la renovación de la suscripción, respectivamente.

## ¡Importante!

* Mantén tu clave privada segura. ¡No la compartas con nadie!
* Asegúrate de que tu información de configuración sea correcta para que el script funcione.
* Los Tokens JWT tienen un tiempo de expiración, en este caso 20 minutos. Si el token expira, tendrás que generar uno nuevo.
* Este código no maneja todos los posibles errores, por lo que podría ser necesario agregar más manejo de errores para uso en producción.

¡Espero que esto te ayude a entender cómo funciona el código! Si tienes más preguntas, ¡no dudes en preguntar!