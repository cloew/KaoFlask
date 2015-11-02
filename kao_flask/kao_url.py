import posixpath

class KaoURL:
    """ Represents a URL string """
    
    def __init__(self, url, parent=None):
        """ Initialize the URL with the url """
        self.flaskUrl = url
        self.nestIn(parent)
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
            self.url += urlPiece
            if i != len(urlPieces)-1:
                self._url += "{}"
                
    @property
    def url(self):
        """ Return the Flask url """
        return self.flaskUrl
        
    def build(self, **kwargs):
        """ Build the url replacing the arguments properly """
        url = self._url.format(*[kwargs[argument] for argument in self.arguments])
        if self.parent is not None:
            url = posixpath(self.parent.build(**kwargs), url)
        return url
        
    def nest(self, *urls):
        """ Nest the given Urls inside this Url """
        for url in urls:
            url.nestIn(self)
        
    def nestIn(self, parent):
        """ Nest this Url in the parent Url """
        self.parent = parent