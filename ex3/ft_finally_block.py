class PlantNameError(Exception):
	pass
def test_name_plant(name: str) -> None:
	if name is None:
		raise PlantNameError(f"Error: Cannot water {name} - invalid plant!")
	else:
		print(f"Watering {name}")
def main():
	print("=== Garden Watering System ===")
	
	plants = ["tomato", "lettuce", "carrots"]
	print("\nTesting normal watering...")
	try:
		print("Opening watering system")
		for plant in plants:
			test_name_plant(plant)
	except PlantNameError as e:
		print(e)
	finally:
		print("Closing watering system (cleanup)")
	print("Watering completed successfully")
	print("\nTesting with error...")
	plants_error = ["tomato", None]
	try:
		print("Opening watering system")
		for plant in plants_error:
			test_name_plant(plant)
	except PlantNameError as e:
		print(e)
	finally:
		print("Closing watering system (cleanup)")
	print("\nCleanup always happens, even with errors!")
if __name__ == "__main__":
	main()
