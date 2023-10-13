from telethon import TelegramClient, events

api_id = 8857035
api_hash = "d6324f28355dffb7ca2cbb27d5d7cd53"

# Lista chat da cui recuperare i messaggi da inoltrare.
from_chats = [-1001201251271,-1001280296873, -1001692297563]
# Chat a cui inoltrare.
to_chat = -1001969696852

# Istanza del Client.
client = TelegramClient('Sessione', api_id, api_hash)

# Gestione evento. Quando arriva un nuovo messaggio al client (events.NewMessage), recupero l'id della chat in cui è arrivato,
# se l'id è presente nella lista precedente, tramite metodo forward_messages inoltro il messaggio alla chat di destinazione.
@client.on(events.NewMessage)
async def my_event_handler(event):
    chat_id = event.chat_id
    if chat_id in from_chats:
        if ('acquisto'       in event.message.text.lower() 
            or 'only buy'    in event.message.text.lower() 
            or 'solo ordine' in event.message.text.lower() 
            or 'commissione' in event.message.text.lower() 
            or 'regalo'      in event.message.text.lower()):
            await client.forward_messages(to_chat, event.message)

# Starto il client e lo runno finchè non si ha disconnessione.
client.start()
client.run_until_disconnected()