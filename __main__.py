from pyrogram import Client
from task_manager import TaskManagerThread, TaskManager

import argparse

parser = argparse.ArgumentParser(description='Start an assistent work with some params')
parser.add_argument('-tmresume', action='store', type=str)

app = Client(
    "Bot_Nikita",
    plugins=dict(root='plugins'),
    config_file='bot_config.ini',
    workdir='.',
    parse_mode="markdown"
)


tm = TaskManager()
app.tm_thread = TaskManagerThread(tm)

app.run()
