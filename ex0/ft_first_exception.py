def check_temperature(temp_str: str):
	try:
	temp_int = int(temp_str)	
		if 0 <= temp_int <= 40:
			print(f"Temperature {temp_int}°C is perfect for plants!")
		elif temp_int < 0:
			print(f"Error: {temp_int} is too cold for plants (min 0°C)")
		else:
			print(f"Error: {temp_int} is too hot for plants (max 40°C)")
	except ValueError:
		print(f"Error: '{temp_str}' is not a valid number")
if __name__ == "__main__":
	print("=== Garden Temperature Checker ===")
	print(" ")
	temperatures = [25, 'abc', 100, -50]
	for temp in temperatures:
		print(f"Testing tempterature: {temp}")
		check_temperature(temp)
		print(" ")
	print("All tests completed - program didn't crash!")
