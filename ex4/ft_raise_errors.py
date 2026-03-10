def check_plant_health(plant_name: str, water_level: int, sunlight_hours: int):
	if plant_name == None or len(plant_name) == 0:
		raise ValueError("Error: Plant name cannot be empty!")
	if (1 <= water_level <= 10) and (2 <= sunlight_hours <= 12):
		print(f"The Plant '{plant_name}' is healthy!")
	if (water_level < 1 or water_level > 10):
		raise ValueError(f"Error: Water level {water_level} is too high (max 10)")
	if (sunlight_hours < 2 or sunlight_hours > 12):
		raise ValueError (f"Error: Sunlight hours {sunlight_hours} is too low (min 2)")

def test_plant():
	print("=== Garden Plant Health Checker ===")
	print("\nTesting good values...")
	check_plant_health("tomato", 7, 8)
	try:
		print("\nTesting empty plant name...")
		check_plant_health("", 7, 8)
	except ValueError as e:
		print(e)
	try:	
		print("\nTesting bad water level...")
		check_plant_health("tomato", 15, 8)
	except ValueError as e:
		print(e)
	try:
		print("\nTesting bad sunlight hours...")
		check_plant_health("tomato", 7, 0)
	except ValueError as e:
		print(e)
	print("\nAll error raising tests completed!")

if __name__ == "__main__":
	test_plant()
