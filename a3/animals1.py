class dog():
	legs = 4
	eyes = 2
	def __init__(self,name,breed,gender):
		self.name = name #Public Member
		self._breed = breed #Protected Member
		self.__gender = gender #Private Member
		
	def get_breed(self):
		return self._breed
		
	def set_breed(self,breed):
		self._breed = breed
		
	def get_gender(self):
		return self.__gender
		
	def set_gender(self,gender):
		self.__gender = gender
		
	def eating(self):
		print("Diet Type: carnivores")
		
	def speak(self):
		print("Sound: bark")
	
class cat():
	legs = 4
	eyes = 2
	def __init__(self, name, breed, gender):
		self.name = name
		self._breed = breed
		self.__gender = gender
		
	def get_breed(self):
		return self._breed
		
	def set_breed(self,breed):
		self._breed = breed
		
	def get_gender(self):
		return self.__gender
		
	def set_gender(self,gender):
		self.__gender = gender
		
	def eating(self):
		print("Diet Type: carnivores")
		
	def speak(self):
		print("Sound: meow")
	
class cow():
	legs = 4
	eyes = 2
	def __init__(self, name,color):
		self.name = name
		self._color = color
		
	def get_color(self):
		return self._color
		
	def set_color(self,color):
		self._color = color
		
	def eating(self):
		print("Diet Type: herbivores")
		
	def speak(self):
		print("Sound: moo")
		
class pig():
	legs = 4
	eyes = 2
	def __init__(self, name, gender,weight):
		self.name = name
		self.gender = gender
		self._weight = weight
		
		
	def get_weight(self):
		return self._weight
		
	def set_weight(self,weight):
		self._weight = weight
		
	def eating(self):
		print("Diet Type: omnivores")
		
	def speak(self):
		print("Sound: oink")

class giraffe():
	legs = 4
	eyes = 2
	def __init__(self, name, gender, height, spotted = "True"):
		self.name = name
		self.gender = gender
		self.spotted = spotted
		self._height = height
		
	def get_height(self):
		return self._height
		
	def set_height(self,height):
		self._height = height
		
	def eating(self):
		print("Diet Type: herbivores")
		
	def speak(self):
		print("Sound: bleat")
		
class lion():
	legs = 4
	eyes = 2
	def __init__(self, name, gender, weight):
		self.name = name
		self.gender = gender
		self._weight = weight
		
	def get_weight(self):
		return self._weight
		
	def set_weight(self,weight):
		self._weight = weight
		
	def eating(self):
		print("Diet Type: carnivores")
	def speak(self):
		print("Sound: roars")
	
class deer():
	legs = 4
	eyes = 2
	def __init__(self, name, gender, spotted ):
		self.name = name
		self.gender = gender
		self._spotted = spotted
	
	def get_spotted(self):
		return self._spotted
		
	def set_spotted(self,spotted):
		self._spotted = spotted	
		
	def eating(self):
		print("Diet Type: herbivores")
		
	def speak(self):
		print("Sound: bleat")
	
class horse():
	legs = 4
	eyes = 2
	def __init__(self, name, color, age, gender):
		self.name = name
		self.color = color
		self._age = age
		self.gender = gender
		
	def get_age(self):
		return self._age
		
	def set_age(self,age):
		self._age = age
	
	def eating(self):
		print("Diet Type: herbivores")
		
	def speak(self):
		print("Sound: neigh")
	
class monkey():
	legs = 4
	eyes = 2
	def __init__(self, name, category, age, gender):
		self.name = name
		self._category = category #Can be old world type or new world type
		self.age = age
		self.gender = gender
		
	def get_category(self):
		return self._category
		
	def set_category(self,category):
		self._category = category
	
	def eating(self):
		print("Diet Type: omnivores")
		
	def speak(self):
		print("Sound: chatter")
		
class tiger():
	legs = 4
	eyes = 2
	def __init__(self, name, color, age, gender,striped = 'True'):
		self.name = name
		self._color = color
		self.age = age
		self.gender = gender
		self.striped = striped
	
	def get_color(self):
		return self._color
		
	def set_color(self,color):
		self._color = color
	
	def eating(self):
		print("Diet Type: carnivores")
		
	def speak(self):
		print("Sound: roar and growl")
		
		
		
print("DOG")
d = dog("Happy","Pomerian","Male")
print("Name:{}".format(d.name)) #Name is a public member and can be accessed directly
print("Breed:{}".format(d.get_breed())) #Breed is a protected member and can't be accessed directly
print("Gender: {}".format(d.get_gender()))
d.eating()
d.speak()

print("\n")
		
print("CAT")
c = cat("Rosie","Persian", "Female")
print("Name: {}".format(c.name))
print("Breed:{}".format(c.get_breed()))
print("Gender: {}".format(c.get_gender()))
c.eating()
c.speak()

print("\n")
		
print("COW")
w = cow("Mel","White")
print("Name: {}".format(w.name))
print("Color: {}".format(w.get_color()))
w.eating()
w.speak()

	



