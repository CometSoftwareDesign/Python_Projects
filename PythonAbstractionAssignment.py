

from abc import ABC, abstractmethod

class song(ABC):
       def songtype(self, genre):
              print("You're favorite song type is:",genre)
              #this function is telling you to put in an argument,
              #but not the data that must be put in. 
       @abstractmethod
       def secretsong(self, genre):
               pass

class songtype1(song):
       #here we find out what singer you really like. 
       def secretsong(self,genre):
              print("You really like {}, but it's a secret.".format(genre))


obj = songtype1()
obj.songtype("Country")
obj.secretsong("Carrie Underwood")
