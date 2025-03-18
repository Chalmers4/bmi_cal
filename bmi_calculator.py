def calculate_bmi(height_feet, height_inches, weight_pounds):
    """
    Calculate BMI based on height (feet and inches) and weight (pounds).
    Formula: BMI = (weight / (height_inches)^2) * 703
    """
    height_total_inches = height_feet * 12 + height_inches
    bmi = (weight_pounds / (height_total_inches ** 2)) * 703
    return round(bmi, 1)  # Round to one decimal place


def get_bmi_category(bmi):
    """
    Determine the BMI category based on the BMI value.
    """
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi <= 24.9:
        return "Normal weight"
    elif 25 <= bmi <= 29.9:
        return "Overweight"
    else:
        return "Obese"


def run_bmi_calculator():
    """
    Command-line interface for the BMI calculator.
    """
    print("Welcome to the BMI Calculator!")
    height_feet = int(input("Enter your height (feet): "))
    height_inches = int(input("Enter your height (inches): "))
    weight_pounds = float(input("Enter your weight (pounds): "))

    bmi = calculate_bmi(height_feet, height_inches, weight_pounds)
    category = get_bmi_category(bmi)

    print(f"Your BMI is: {bmi} ({category})")


if __name__ == "__main__":
    run_bmi_calculator()