from flask.ext.stormpath import StormpathManager

class StormpathExtension:
    """ Represents an extension to add Stormpath characteristics to the Flask server """
    
    def initialize(self, server):
        """ Initialize the Server with the extension """
        server.stormpathManager = StormpathManager(server.app)