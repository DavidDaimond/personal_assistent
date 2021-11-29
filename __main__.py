from pyrogram import Client
from task_manager import TaskManagerThread, TaskManager


app = Client(
    "Bot_Nikita",
    plugins=dict(root='plugins'),
    config_file='bot_config.ini',
    workdir='.',
    parse_mode="markdown"
)

app.tm_thread = TaskManagerThread(TaskManager())

app.run()
