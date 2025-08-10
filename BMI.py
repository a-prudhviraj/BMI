import sys
from colorama import Fore, init

# Initialize colorama for colored terminal output
init(autoreset=True)


def get_gender():
    while True:
        gender_choice = input("👨 Male or 👩 Female? (m/f): ").strip().lower()
        if gender_choice in ("m", "f"):
            return "Male" if gender_choice == "m" else "Female"
        print(Fore.RED + "❌ Please enter 'm' for male 👨 or 'f' for female 👩.")


def get_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value > 0:
                return value
            print(Fore.RED + "❌ Please enter a positive number.")
        except ValueError:
            print(Fore.RED + "❌ Invalid input, please enter a numeric value.")


def get_height():
    print("\n📏 Choose height unit (default is meters):")
    print("1️⃣  Meters (m) [default]")
    print("2️⃣  Centimeters (cm)")
    print("3️⃣  Feet (ft)")
    print("4️⃣  Inches (in)")
    unit = input("➡️  Enter choice (1-4, press Enter for default): ").strip() or "1"

    if unit == "1":
        return get_float("📐 Enter height in meters: ")
    elif unit == "2":
        return get_float("📐 Enter height in centimeters: ") / 100
    elif unit == "3":
        return get_float("📐 Enter height in feet: ") * 0.3048
    elif unit == "4":
        return get_float("📐 Enter height in inches: ") * 0.0254
    else:
        print(Fore.RED + "❌ Invalid choice! Using meters by default.")
        return get_float("📐 Enter height in meters: ")


def get_weight():
    print("\n⚖️  Choose weight unit (default is kilograms):")
    print("1️⃣  Kilograms (kg) [default]")
    print("2️⃣  Pounds (lb)")
    unit = input("➡️  Enter choice (1-2, press Enter for default): ").strip() or "1"

    if unit == "1":
        return get_float("⚖️  Enter weight in kilograms: ")
    elif unit == "2":
        return get_float("⚖️  Enter weight in pounds: ") * 0.453592
    else:
        print(Fore.RED + "❌ Invalid choice! Using kilograms by default.")
        return get_float("⚖️  Enter weight in kilograms: ")


def calculate_bmi(weight, height):
    return weight / (height ** 2)


def determine_category(bmi, gender):
    if gender == "Male":
        thresholds = [
            (18.5, "Underweight", "🍽️ Eat nutrient-rich meals."),
            (25, "Normal weight", "🎉 Great job maintaining your health!"),
            (30, "Overweight", "🚶‍♂️ Exercise regularly & eat balanced meals."),
            (float("inf"), "Obese", "🩺 Consult a healthcare provider."),
        ]
    else:
        thresholds = [
            (18, "Underweight", "🍽️ Eat nutrient-rich meals."),
            (24, "Normal weight", "🎉 Great job maintaining your health!"),
            (29, "Overweight", "🚶‍♀️ Exercise regularly & eat balanced meals."),
            (float("inf"), "Obese", "🩺 Consult a healthcare provider."),
        ]

    for limit, category, advice in thresholds:
        if bmi < limit:
            return category, advice


def display_bmi_chart(gender):
    print(Fore.CYAN + "\n📋 BMI Categories:")
    if gender == "Male":
        print("Underweight: Less than 18.5")
        print("Normal weight: 18.5 – 24.9")
        print("Overweight: 25 – 29.9")
        print("Obese     : 30 or more")
    else:
        print("Underweight: Less than 18")
        print("Normal weight: 18 – 23.9")
        print("Overweight: 24 – 28.9")
        print("Obese     : 29 or more")


def main():
    print(Fore.CYAN + "💖 Welcome to the Universal BMI Calculator 💖\n")

    while True:
        gender = get_gender()
        height = get_height()
        weight = get_weight()

        bmi = calculate_bmi(weight, height)
        category, advice = determine_category(bmi, gender)

        print(Fore.YELLOW + f"\n📊 Your BMI is {bmi:.2f} ({category})")
        display_bmi_chart(gender)
        print(Fore.GREEN + f"\n⚠️ {advice}")
        print(Fore.MAGENTA + "✨ Created with care 🌙 by Aenugula Prudhviraj 🐘")
        print(Fore.CYAN + "\n👋 Thank you for using the BMI Calculator! Stay healthy! 💪🐼")

        # Show recalculation prompt and exit option simultaneously
        user_input = input(Fore.BLUE + "\n🔄 Do you want to calculate again? (y/n) or press Enter to exit: ").strip().lower()
        if user_input != "y":
            break


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nStay healthy! 💪🐼")
