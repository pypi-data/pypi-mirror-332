from .Queue.Queue import Queue
from .Queue.Deque import Deque
from .Tree import Tree

class Wpyd:
    @staticmethod
    def Queue():
        """
        Return an instance of a queue data structure
        """
        return Queue()
    @staticmethod
    def Deque():
        """
        Return an instance of a double ended queue data structure
        """
        return Deque()
    @staticmethod
    def Tree():
        """
        Return an instance of a tree data structure
        """
        return Tree()


__all__ = ['Deque', 'Queue', 'Tree']