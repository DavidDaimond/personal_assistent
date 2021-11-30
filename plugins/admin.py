from pyrogram import Client, filters
from config import ADMINS

import pickle


@Client.on_message(filters.private & filters.incoming & filters.command(['shutdown']) & filters.user(ADMINS))
def _shutdown(client, message):
    client.send_message(chat_id=message.chat.id,
                        text="WHY WOULD YOU DO THIS?..... 😭😭😭\n\nNoo.......",
                        )
    client.stop()
    exit()


@Client.on_message(filters.private & filters.incoming & filters.command(['save_config']) & filters.user(ADMINS))
def _save_configuration(client, message):
    client.send_message(chat_id=message.chat.id,
                        text="Save data....",
                        )

    with open('tasks.pkl', 'wb') as save_file:
        pickle.dump(client.tm_thread.tm, save_file)

