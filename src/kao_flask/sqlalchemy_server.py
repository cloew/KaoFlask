from kao_flask.server import Server

from flask.ext.sqlalchemy import SQLAlchemy

class SqlAlchemyServer(Server):
    """ Represents a Sql Alchemy based Falsk Server """
    
    def __init__(self, name, config, routes=[]):
        """ Initialize the Server """
        Server.__init__(name, routes=routes)
        self.app.config.from_object(config)
        self.db = SQLAlchemy(self.app)