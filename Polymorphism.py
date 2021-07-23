


#parent class
class Galaxy:
       name = 'Azuli'
       Solar_Systems = 1000000
       Planets = 340
       Moons = 8000000000
       Will_Die = True


       def information(self):
              msg = "\nYou are the {}  and you have \n{} Solar Systems, \n{} Planets, {} Moons and you will die.{}".format(self.name,self.Solar_Systems, self.Planets, self.Moons, self.Will_Die)
              return msg 



#child class
class Solar_System(Galaxy):
       name = "\nApollon"
       Solar_Systems = 0
       Planets = 12
       Moons = 233
       Has_Black_Holes = False

       def welcome(self):
              msg = "\n Welcome to Apollon. You have Black Holes. {}. Just Kidding.".format(Solar_System.Has_Black_Holes)
              return msg
       

# another child instance

class Planet(Galaxy):
       name = "\nSolaris"
       Solar_System = "Apollon"
       Planets = 0
       Moons = 32
       origin = "Built by the Dolphins."

       def Welcome(self):
              msg = "\nCurrent home of Arthur Dent and {}".format(Planet.origin)
              return msg


if __name__ == "__main__":
       solsys = Solar_System()
       print(solsys.information())
       print(solsys.welcome())

       planet = Planet()
       print(planet.information())
       print(planet.Welcome())

      
