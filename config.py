import logging

# This is a minimal configuration to get you started with the Text mode.
# If you want to connect Errbot to chat services, checkout
# the options in the more complete config-template.py from here:
# https://raw.githubusercontent.com/errbotio/errbot/master/errbot/config-template.py

BACKEND = 'Slack'
BOT_DATA_DIR = r'/Users/shashank.koppar/Documents/errbot/data'
BOT_EXTRA_PLUGIN_DIR = '/Users/shashank.koppar/Documents/errbot/plugins'

BOT_LOG_FILE = r'/Users/shashank.koppar/Documents/errbot/errbot.log'
BOT_LOG_LEVEL = logging.DEBUG

BOT_ADMINS = ('@shashank', )  # !! Don't leave that to "CHANGE ME" if you connect your errbot to a chat system !!

BOT_ALT_PREFIXES = ('@migration_bot',)

BOT_IDENTITY = {
    'token': 'xoxb-148530697060-hVFV0xHk0Qn3kq3opnO7YvcG',
}

CHATROOM_PRESENCE = () ;

JENKINS_URL= "http://100.73.38.199:8080"
JENKINS_USERNAME= "shashank.koppar"
JENKINS_PASSWORD= "8ec4a8003584bbf1a72418605f90d322"