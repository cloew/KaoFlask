from flask import Flask

class Server:
    """ Represents the Flask Server """
    
    def __init__(self, name):
        """ Initialize the Server """
        self.app = Flask(name)
        
    def run(self):
        """ Run the server """
        self.app.run()