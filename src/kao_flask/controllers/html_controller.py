from flask import make_response

class HTMLController:
    """ Represents a Controller for an HTML page """
    
    def __init__(self, pathToPage):
        """ Initialize the HTML Controller with the path to the Page """
        self.pathToPage = pathToPage
    
    def perform(self):
        """ Perform the Controller action """
        return make_response(open(self.pathToPage).read())