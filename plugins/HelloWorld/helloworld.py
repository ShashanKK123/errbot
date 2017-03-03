from errbot import BotPlugin, botcmd

class HelloWorld(BotPlugin):
    """Example 'Hello, world!' plugin for Errbot"""

    @botcmd
    def helloworld(self, msg, args):
        """Say hello to the world"""
        return "Hello, " + format(msg.frm)
