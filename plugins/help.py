from pyrogram import Client, filters
from config import Messages as msg


@Client.on_message(filters.private & filters.incoming & filters.command(['start']))
def _start(client, message):
    client.send_message(chat_id=message.chat.id,
                        text=msg.START_MSG.format(message.from_user.mention),
                        reply_to_message_id=message.message_id
                        )


@Client.on_message(filters.private & filters.incoming & filters.command(['help']))
def _start(client, message):
    client.send_message(chat_id=message.chat.id,
                        text=msg.HELP_MSG,
                        reply_to_message_id=message.message_id
                        )
