from pyrogram import Client, filters


def task_func(client, user, msg):
    client.send_message(
        chat_id=user.id,
        text=msg
    )


@Client.on_message(filters.private & filters.incoming & filters.command(['new_task']))
def _new_task(client, message):
    pass
