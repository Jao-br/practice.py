CityName = input("Input City Name: ").lower()

if any(x in CityName for x in ["joão", "lucas", "mateus", "santos", "santo", "são"]):
    print("This Brazilian city does have a religious name.")
else:
    print("This Brazilian city does NOT have a religious name.")