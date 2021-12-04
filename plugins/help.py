from pyrogram import Client, filters
from commands import start_func, help_func


@Client.on_message(filters.private & filters.incoming & filters.command(['start']))
def _start(client, message):
    start_func(client, message)


@Client.on_message(filters.private & filters.incoming & filters.command(['help']))
def _help(client, message):
    help_func(client, message)
