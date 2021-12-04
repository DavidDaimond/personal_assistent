from config import Messages as msg
from config import save_file_name
import pickle


def start_func(client, message):
    client.send_message(chat_id=message.chat.id,
                        text=msg.START_MSG.format(message.from_user.mention),
                        reply_to_message_id=message.message_id
                        )


def help_func(client, message):
    client.send_message(chat_id=message.chat.id,
                        text=msg.HELP_MSG,
                        reply_to_message_id=message.message_id
                        )


def shutdown_func(client, message):
    client.send_message(chat_id=message.chat.id,
                        text="WHY WOULD YOU DO THIS?..... 😭😭😭\n\nNoo.......",
                        )
    client.stop()
    exit()


def save_config_func(client, message):
    client.send_message(chat_id=message.chat.id,
                        text="Save data....",
                        )

    with open(save_file_name, 'wb') as save_file:
        pickle.dump(client.tm_thread.tm, save_file)


commands_dict = {
    'start': start_func,
    'help': help_func,
    'shutdown': shutdown_func,
    'save_configuration': save_config_func
}
