# Import needed by Telethon
from telethon import TelegramClient, events

# Personal ID and HASH required for interaction with your Telegram account. 
api_id = your_id
api_hash = "your_hash"

# Chat list from which to retrieve messages to forward. Your ID must have the form: -id_number,
# Write IDs without " ". You can retrieve the IDs via the url on Telegram Web or by using IDBot on Telegram itself.
from_chats = [chat_id1, chat_id2, chat_id3]
# Chat to forward to.
to_chat = chat_id_to

# Client Instance.
client = TelegramClient('Sessione', api_id, api_hash)

# Event handling. When a new message arrives at the client (events.NewMessage), I retrieve the id of the chat where it arrived,
# if the id is in the previous list  and the message contains one of the following words or phrase, via forward_messages method 
# I forward the message to the destination chat.
@client.on(events.NewMessage)
async def my_event_handler(event):
    chat_id = event.chat_id
    if chat_id in from_chats:
        if ('astring1'    in event.message.text.lower() 
             or 'string2' in event.message.text.lower() 
             or 'string3' in event.message.text.lower() 
             or 'string4' in event.message.text.lower() 
             or 'string5' in event.message.text.lower()):
             await client.forward_messages(to_chat, event.message)

# Start the client and run it until there is no disconnection.
client.start()
client.run_until_disconnected()
