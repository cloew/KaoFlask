from kao_flask.server import Server
from kao_flask.database import db

class SqlAlchemyServer(Server):
    """ Represents a Sql Alchemy based Flask Server """
    
    def __init__(self, name, config, routes=[]):
        """ Initialize the Server """
        Server.__init__(self, name, routes=routes)
        self.app.config.from_object(config)
        
        db.init_app(self.app)
        self.db = db