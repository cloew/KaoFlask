import posixpath

class NestedApp:
    """ Represents a Nested App so that routes are added at a nested URL """
    
    def __init__(self, app, prefix):
        """ Initialize with the prefix """
        self.app = app
        self.prefix = prefix
        
    def add_url_rule(self, url, *args, **kwargs):
        """ Add the Url by first adding the prefix """
        self.app.add_url_rule(posixpath.join(self.prefix, url), *args, **kwargs)