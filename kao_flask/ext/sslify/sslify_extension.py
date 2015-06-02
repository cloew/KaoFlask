from flask_sslify import SSLify

class SslifyExtension:
    """ Represents an extension to setup the Server for SSLify integration """

    def initialize(self, server):
        """ Initialize the Server with the extension """
        server.sslify = SSLify(server.app)