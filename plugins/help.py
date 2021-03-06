from slackbot.bot import respond_to, listen_to
import json

def load_help_json():
    with open('plugins/functions.json') as f:
        functions = json.load(f)
    return functions

@respond_to(r'^help$')
@respond_to(r'^help (.*)')
@listen_to(r'^!help$')
@listen_to(r'^!help (.*)')
def help(message, helpfunction=None):
    functions = load_help_json()
    if helpfunction is None:
        reply = "Valid commands: "
        for function, text in functions.items():
            reply += "%s " % function
        reply += '\n use the help command for more information'
        message.reply(reply)

    elif helpfunction in functions:
        message.reply("%s: %s" %(helpfunction, functions[helpfunction]))
    else:
        message.reply('I don\'t know that command')