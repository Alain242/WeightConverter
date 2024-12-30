def convert_weight():
    """Converts weight between kilograms and pounds."""

    try:
        weight = float(input("Enter your weight: "))
    except ValueError:
        print("Invalid input. Please enter a numerical weight.")
        return  # Exit the function if input is invalid

    unit = input("Kilograms or Pounds? (k or l): ").lower()

    if unit == "k":
        converted_weight = weight * 2.205
        converted_unit = "lbs."
        print(f"Your weight is: {converted_weight:.2f} {converted_unit}")  # Format to 2 decimal places

    elif unit == "l":
        converted_weight = weight / 2.205  # Correct conversion: divide by 2.205
        converted_unit = "kgs."
        print(f"Your weight is: {converted_weight:.2f} {converted_unit}")

    else:
        print(f"Invalid unit: '{unit}'. Please enter 'k' for kilograms or 'l' for pounds.")

if __name__ == "__main__":
    convert_weight()