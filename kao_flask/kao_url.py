
class KaoURL:
    """ Represents a URL string """
    
    def __init__(self, route):
        """ Initialize the URL with the route """
        self.flaskUrl = route
        pieces = route.split('<')
        urlPieces = [pieces[0]]
        self.arguments = []
        for piece in pieces[1:]:
            argPieces = piece.split('>')
            self.arguments.append(argPieces[0].split(':')[1] if ':' in argPieces[0] else argPieces[0])
            urlPieces.append(argPieces[1])
            
        self.url = ""
        for i, urlPiece in enumerate(urlPieces):
            self.url += urlPiece
            if i != len(urlPieces)-1:
                self.url += "{}"
                
    @property
    def route(self):
        """ Return the Flask route """
        return self.flaskUrl
        
    def build(self, **kwargs):
        """ Build the url replacing the arguments properly """
        return self.url.format(*[kwargs[argument] for argument in self.arguments])