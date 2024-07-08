from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from django.conf import settings

#Funcion para enviar mensaje al slack, con canal definido por defecto en las settings, junto con el token

def enviar_slack(mensaje, canal=settings.SLACK_CHANNEL):
    client = WebClient(token=settings.SLACK_TOKEN)
    try:
        response = client.chat_postMessage(channel=canal, text=mensaje)
        return response
    except SlackApiError as e:
        print(f"error: {e.response['error']}")