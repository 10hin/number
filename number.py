from rational import Rational

class Number(object):
    @staticmethod
    def isnumber(obj):
        if isinstance(obj, int):
            return True
        if isinstance(obj, Rational):
            return True
        return False
