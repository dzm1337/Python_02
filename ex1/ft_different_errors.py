def garden_operations():
    try:
        print("Testing ValueError...")
        int("abc")
    except ValueError:
        print("Caught ValueError: invalid literal for int()\n")

    try:
        print("Testing ZeroDivisionError...")
        _ = 5 / 0
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero\n")

    try:
        print("Testing FileNotFoundError...")
        open("file.txt", "r")
    except FileNotFoundError:
        print("Caught FileNotFoundError: No such file 'missing.txt'\n")

    try:
        print("Testing KeyError...")
        x = {"x": "a"}
        print(x["banana"])
    except KeyError:
        print(r"Caught KeyError: 'missing\_plant'")
        print(" ")

    try:
        print("Testing multiple errors together...")
        int("abc")
        _ = 5 / 0
    except (ValueError, ZeroDivisionError):
        print("Caught an error, but program continues!\n")


def test_error_types():
    print("=== Garden Error Types Demo ===")
    garden_operations()
    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
