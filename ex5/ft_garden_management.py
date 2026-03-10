class ErrorNamePlant(Exception):
	pass

class ErrorWaterLevel(ErrorNamePlant):
	pass

class ErrorSunlightHours(ErrorNamePlant):
	pass

class GardenManager():
	def __init__(self):
		self._plants = [] 
		
	def add_plant(self, plant):
		if not plant:
			raise ErrorNamePlant(f"Error adding plant: Plant name cannot be empty!")
		print(f"Added {plant} to Garden succesfully")
		self._plants.append(plant)

	def water_plant(self, plant):
		if not plant:
			raise ErrorNamePlant(f"Error watering plant: Plant name cannot be empty!")
		if plant not in self._plants:
			self._plants.append(plant)
		print(f"Watering {plant} - success")

	def plant_health(self, plant: str, water_level: int, sunlight_hours: int):
		if not plant:
			raise ErrorNamePlant(f"Error: The name cannot be empty!")
		if not (1 <= water_level <= 10):
			raise ErrorWaterLevel(f"Error: Water level {water_level} is too high (max 10)")
		if not (2 <= sunlight_hours <= 12):
			raise ErrorSunlightHours(f"Error: Sunlight hours {sunlight_hours} is too high (max 12)")
		print(f"{plant}: healthy (water: {water_level}, sun: {sunlight_hours})")

	@staticmethod
	def water_test(water_value: int):
		if (water_value < 50):
			raise Exception(f"Caught GardenError: Not enough water in tank")
		else:
			print("There's enough water in the tank!")
		print("System recovered and continuing...")

def test_garden_management():
	print("=== Garden Management System ===")
	garden = GardenManager()
	plants = ["tomato", "lettuce", ""]
	
	try:
		print("\nAdding plants to garden...")
		for plant in plants:
			garden.add_plant(plant)
	except ErrorNamePlant as e:
		print(e)	

	plants = ["tomato", "lettuce"]
	print("\nWatering plants...")
	try:
		print("Opening watering system")
		for plant in plants:
			garden.water_plant(plant)
	except ErrorNamePlant as e:
		print(e)
	finally:
		print("Closing watering system (cleanup)")
	print("\nChecking plant health...")
	try:
		plants = [
		{"plant": "tomato", "water_level": 5, "sunlight_hours": 8},
		{"plant": "lettuce", "water_level": 15, "sunlight_hours": 6}
		]
		for plant in plants:
			garden.plant_health(plant["plant"], plant["water_level"], plant["sunlight_hours"])	
	except (ErrorWaterLevel, ErrorSunlightHours) as e:
		print(e)
	print("\nTesting error recovery...")
	try:
		GardenManager.water_test(48)
	except Exception as e:
		print(e)
	print("System recovered and continuing...")
	print("\nGarden management system test complete!")

if __name__ == "__main__":
	test_garden_management()
