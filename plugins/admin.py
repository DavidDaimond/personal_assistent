from pyrogram import Client, filters
from config import ADMINS
from commands import shutdown_func, save_config_func


@Client.on_message(filters.private & filters.incoming & filters.command(['shutdown']) & filters.user(ADMINS))
def _shutdown(client, message):
    shutdown_func(client, message)


@Client.on_message(filters.private & filters.incoming & filters.command(['save_config']) & filters.user(ADMINS))
def _save_configuration(client, message):
    save_config_func(client, message)

