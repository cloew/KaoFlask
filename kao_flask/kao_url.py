import posixpath

class KaoUrl:
    """ Represents a URL string """
    
    def __init__(self, url):
        """ Initialize the URL with the url """
        self.flaskUrl = url
        self._parseArgs(url)
        
    def _parseArgs(self, url):
        """ Parse and store the arguments embedded in the Url """
        pieces = url.split('<')
        urlPieces = [pieces[0]]
        self.arguments = []
        for piece in pieces[1:]:
            argPieces = piece.split('>')
            self.arguments.append(argPieces[0].split(':')[1] if ':' in argPieces[0] else argPieces[0])
            urlPieces.append(argPieces[1])
            
        self._url = ""
        for i, urlPiece in enumerate(urlPieces):
            self._url += urlPiece
            if i != len(urlPieces)-1:
                self._url += "{}"
                
    @property
    def url(self):
        """ Return the Flask url """
        return self.flaskUrl
        
    def build(self, **kwargs):
        """ Build the url replacing the arguments properly """
        return self._url.format(*[kwargs[argument] for argument in self.arguments])