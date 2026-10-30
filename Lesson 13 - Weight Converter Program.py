weight = int(input("Weight: "))

unit = input("(L)bs or (K)gs: ")

if unit.upper() == "L":
    converted_weight  = weight * 0.45
else:
    converted_weight = weight / 0.45

print(f"Weight in kg: {converted_weight}")