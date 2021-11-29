from pyrogram import Client

app = Client(
    "Bot_Nikita",
    plugins=dict(root='plugins'),
    config_file='bot_config.ini',
    workdir='.',
    parse_mode="markdown"
)

app.run()
