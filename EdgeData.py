from numpy.core import double


class EdgeData:

    def __init__(self, source: int = None, dest: int = None, weight: double = None):
        self.dest = dest
        self.source = source
        self.weight = weight

    def get_src(self):
        return self.source

    def get_dest(self):
        return self.dest

    def get_weight(self):
        return self.weight

    def set_src(self, source: int):
        self.source = source

    def set_dest(self, dest: int):
        self.dest = dest

    def set_weight(self, weight: double):
        self.weight = weight
