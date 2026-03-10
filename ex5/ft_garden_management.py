class ErrorNamePlant(Exception):
	pass

class ErrorWaterLevel(ErrorNamePlant):
	pass

class ErrorSunlightHours(ErrorNamePlant):
	pass

class GardenManager():
	def __init__(self, plants=[]):
		self._plants = plants
		
	def add_plant(self, plant):
		if (len(plant) == 0) or (plant == None):
			raise ErrorNamePlant(f"Error adding plant: Plant name cannot be empty!")
		print(f"Added {plant} to Garden succesfully")
		self._plants.append(plant)
	def water_plant(self, plant):
		if (len(plant) == 0) or (plant == None):
			raise ErrorNamePlant(f"Error watering plant: Plant name cannot be empty!")
		print(f"Watering {plant} - success")
		self._plants.append(plant)
	def plant_health(self, plant: str, water_level: int, sunlight_hours: int):
		if (len(plant) == 0 or plant == None):
			raise ErrorNamePlant(f"Error: The name cannot be empty!")
		if (1 <= water_level <= 10 and 2 <= sunlight_hours <= 12):
			print(f"{plant}: healthy (water: {water_level}, sun: {sunlight_hours})")
		if (water_level > 10):
			raise ErrorWaterLevel(f"Error: Water level {water_level} is too high (max 10)")
		elif (water_level < 1):
			raise ErrorWaterLevel(f"Error: Water level {water_level} is too low (min 1)")
		if (sunlight_hours > 12):
			raise ErrorSunlightHours(f"Error: Sunlight hours {sunlight_hours} is too high (max 12)")
		elif (sunlight_hours < 2):
			raise ErrorSunlightHours(f"Error: Sunlight hours {sunlight_hours} is too low (min 2)")
	@staticmethod
	def water_test(water_value: int):
		if (water_value < 50):
			raise Exception(f"Caught GardenError: Not enough water in tank")
		else:
			print("There's enough water in the tank!")
		print("System recovered and continuing...")

def test_add_plants():
	try:
		print("\nAdding plants to garden...")
		plants = ["TOMATO", "lettuce", "carrot", "sunflower", "rose"]
		garden = GardenManager()
		for plant in plants:
			garden.add_plant(plant.lower())
	except ErrorAddPlant as e:
		print(e)
	try:
		print("\nAdding plants to garden...")
		plants = ["tomato", "lettuce", "", "sunflower", "rose"]
		garden = GardenManager()
		for plant in plants:
			garden.add_plant(plant.lower())
	except ErrorNamePlant as e:
		print(e)

def test_water_plants():
	try:
		print("\nWatering plants...")
		print("Opening watering system")
		plants = ["tomato", "lettuce"]
		garden = GardenManager()
		for plant in plants:
			garden.water_plant(plant)
	except ErrorNamePlant as e:
		print(e)
	finally:
		print("Closing watering system (cleanup)")
	try:
		print("\nWatering plants...")
		print("Opening watering system")
		plants = ["tomato", "lettuce", ""]
		garden = GardenManager()
		for plant in plants:
			garden.water_plant(plant)
	except ErrorNamePlant as e:
		print(e)
	finally:
		print("Closing watering system (cleanup)")	

def test_healthy_plants():
	try:
		print("\nChecking plant health...")
		garden = GardenManager()
		plants = [
		{"plant": "tomato", "water_level": 7, "sunlight_hours": 8},
		{"plant": "lettuce", "water_level": 15, "sunlight_hours": 6}
		]
		for plant in plants:
			garden.plant_health(plant["plant"], plant["water_level"], plant["sunlight_hours"])	
	except (ErrorWaterLevel, ErrorSunlightHours) as e:
		print(e)
	try:
		print("\nChecking plant health...")
		garden = GardenManager()
		plants = [
    		{"plant": "tomato", "water_level": 8, "sunlight_hours": 8},
    		{"plant": "lettuce", "water_level": 6, "sunlight_hours": 5},
  		{"plant": "cactus", "water_level": 2, "sunlight_hours": 10},
    		{"plant": "fern", "water_level": 0, "sunlight_hours": 3},
    		{"plant": "lavender", "water_level": 4, "sunlight_hours": 9}
		]	
		for plant in plants:
			garden.plant_health(plant["plant"], plant["water_level"], plant["sunlight_hours"])	
	except (ErrorWaterLevel, ErrorSunlightHours) as e:
		print(e)

def water_test():
	try:
		print("\nTesting error recovery...")
		GardenManager.water_test(48)
	except Exception as e:
		print(e)
	print("System recovered and continuing...")

def test_garden_management():
	test_add_plants()
	test_water_plants()
	test_healthy_plants()
	water_test()
	
if __name__ == "__main__":
	test_garden_management()
	print("\nGarden management system test complete!")
