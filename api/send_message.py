import pywhatkit
from datetime import datetime, timedelta

num = '+5493517538429'  # Número de destino del mensaje.
msg = '8==D'  # Mensaje.
wait_time = 1  # Tiempo de espera para enviar el mensaje.
add_time = 10  # Para buscar la hora y minuto a la que se envía el mensaje lo toma 5 segundos luego de la hora actual.


def send_a_message():
    """
    Envía un mensaje por Whatsapp.
    """
    try:
        now = datetime.now()
        next_hour = now + timedelta(seconds=add_time)
        hour, minute = next_hour.time().hour, next_hour.time().minute

        print(' ')
        print(f'Hora: {hour} - tipo: {type(hour)} ')
        print(f'Minuto: {minute} - tipo: {type(minute)}')
        print(' ')

        pywhatkit.sendwhatmsg(num, msg, hour, minute, wait_time=wait_time)

        return 'Mensaje enviado.'
    except Exception as e:
        return str(e)


send_a_message()
