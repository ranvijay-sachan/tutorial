import collections

class Lru(objects):
   def __init__(self):
       self.capacity = 5
       self.buffer = collection.Ordereddict()
       self.current_size = 0


   def get(self, key):
       if key in self.buffer:
          return self.buffer[key]
       else:
          return "Not found"
       

   def insert(self, key, value):
       if key in self.buffer:
          return "already exist"
       elif self.current_size < self.capacity:
          self.buffer[key] = value
          self.current_size += 1

       elif self.current_size >= self.capacity:
            self.buffer.pop()
            self.buffer[key] = value




