class PriorityQueue:
        class Node:
                def __init__(self, data, priority, next_node=None):
                        self.__data = data
                        self.__priority = priority
                        self.__next_node = next_node

                def data(self):

                        return self.__data

                def priority(self):

                        return self.__priority

                def get_next(self):

                        return self.__next_node

                def set_next(self, next_node):

                        self.__next_node = next_node

        def __init__(self):
                
                self.__current_size = 0
                self.__head = None

        def offer(self, data, priority):

                if self.is_empty():
                        
                        self.__current_size = 1
                        self.__head = self.Node(data, priority)

                else:

                        c = self.Node(data, priority)

                        if priority >= self.__head.priority():

                                c.set_next(self.__head)                               
                                self.__current_size += 1
                                self.__head = c
                                
                                return
                        
                        i = self.__head

                        while i.get_next() != None and i.get_next().priority() > priority:

                                i = i.get_next()

                        c.set_next(i.get_next())                        
                        self.__current_size += 1
                        i.set_next(c)

                return

        def poll(self):

                if self.is_empty():

                        print("Error: List is empty")

                else:

                        v = self.__head.data()                        
                        self.__current_size -= 1
                        self.__head = self.__head.get_next()

                        return v                    

        def size(self):

                return self.__current_size

        def is_empty(self):

                return self.__current_size == 0

        def __str__(self):

                return "This is a list"


if __name__ == '__main__':

        pass
