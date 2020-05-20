from abc import ABC, abstractmethod

class animal(ABC): #Main Class
	
	legs = 4
	eyes = 2
	def __init__(self,name,age,gender):
		self.name = name 
		self.age = age 
		self.gender = gender 
		
	def get_name(self):
		return self.name
		
	def set_name(self,name):
		self.name = name
		
	def get_age(self):
		return self.age
		
	def set_age(self,age):
		self.age = age
		
	def get_gender(self):
		return self.gender
		
	def set_gender(self,gender):
		self.gender = gender
		
	@abstractmethod
	def get_type(self):
		pass
	
	@abstractmethod	
	def eating(self):
		pass
	
	@abstractmethod
	def speak(self):
		pass
		
class dog(animal):
	
	def __init__(self,name,breed,age,gender):
		animal.__init__(self,name,age,gender) 
		self.breed = breed

	def get_breed(self):
		return self.breed
		
	def set_breed(self,breed):
		self.breed = breed
	
	def get_type(self):
		print("Mammal")
		
	def eating(self):
		print("Diet types: carnivores")
		
	def speak(self):
		print("Sound: bark")
		
class cat(animal):

	def __init__(self,name,color,age,gender):
		animal.__init__(self,name,age,gender)
		self.color = color
		
	def get_color(self):
		return self.color
		
	def set_color(self,color):
		self.color = color
	
	def get_type(self):
		print("Mammal")	
	
	def eating(self):
		print("Diet types: carnivores")
		
	def speak(self):
		print("Sound: meow")
		
class cow(animal):
	
	def __init__(self,name,color,age,gender):
		animal.__init__(self,name,age,gender) 
		self.color = color
		
	def get_color(self):
		return self.color
		
	def set_color(self,color):
		self.color = color
	
	def get_type(self):
		print("Mammal")
		
	def eating(self):
		print("Diet types: herbivores")
		
	def speak(self):
		print("Sound: moo")
		
class pig(animal):
	
	def __init__(self,name,gender,age,weight):
		animal.__init__(self,name,age,gender) 
		self.weight = weight
		
	def get_weight(self):
		return self.weight
		
	def set_weight(self,weight):
		self.weight = weight
		
	def get_type(self):
		print("Mammal")
		
	def eating(self):
		print("Diet types: omnivores")
		
	def speak(self):
		print("Sound: oink")

class giraffe(animal):
	
	def __init__(self, name, gender, height,age, spotted=True):
		animal.__init__(self,name,age,gender) 
		self.height = height
	
	def get_height(self):
		return self.height
		
	def set_height(self,height):
		self.height = height
	
	def get_type(self):
		print("Mammal")
	
	def eating(self):
		print("Diet types: herbivores")
		
	def speak(self):
		print("Sound: bleat")
	
class lion(cat): #Lion inherits from Cat

	def __init__(self,name,gender,age,weight):
		cat.__init__(self,"","","","")
		self.weight = weight
		
	def get_weight(self):
		return self.weight
		
	def set_height(self,weight):
		self.weight = weight
	
	def eating(self):
		print("Diet types: carnivores")
		
	def speak(self):
		print("Sound: roars")
	
class deer(animal):

	def __init__(self, name, gender,age, spotted):
		animal.__init__(self,name,age,gender) 
		self.spotted = spotted
		
	def get_spotted(self):
		return self.spotted
		
	def set_spotted(self,spotted):
		self.spotted = spotted
		
	def get_type(self):
		print("Mammal")
			
	def eating(self):
		print("Diet types: herbivores")
		
	def speak(self):
		print("Sound: bleat")
	
class horse(animal):
	
	def __init__(self, name, color, age, gender):
		animal.__init__(self,name,age,gender) 
		self.color = color
	
	def get_color(self):
		return self.color
		
	def set_color(self,color):
		self.color = color
			
	def get_type(self):
		print("Mammal") 
		
	def eating(self):
		print("Diet types: herbivores")
		
	def speak(self):
		print("Sound: neigh")
	
class monkey(animal):
	
	def __init__(self, name, category, age, gender):
		animal.__init__(self,name,age,gender) 
		self.category = category #Can be old world types or new world types
		
	def get_category(self):
		return self.category
		
	def set_category(self,category):
		self.category = category
	
	def get_type(self):
		print("Mammal")
	
	def eating(self):
		print("Diet types: omnivores")
		
	def speak(self):
		print("Sound: chatter")
		
class tiger(cat): #Tiger inherits from Cat
	
	def __init__(self, name, age, gender,striped):
		cat.__init__(self,"","","","")
		self.striped = striped
		
	def get_striped(self):
		return self.striped
		
	def set_striped(self,striped):
		self.striped = striped

	def eating(self):
		print("Diet types: carnivores")
		
	def speak(self):
		print("Sound: roar and growl")
		


