class TDEECalculator:
    def __init__(self):
        self.sex = ""
        self.weight = 0
        self.height = 0
        self.age = 0
        self.PAL = 0
        self.BMR = 0

    def receive_info(self):
        self.sex = input("Are you Male or Female? ").lower()
        self.weight = float(input("What is your weight in Kilograms? "))
        self.height = float(input("What is your height in Centimeters? "))
        self.age = int(input("What is your age? "))
        self.PAL = input("""\nEnter 1 for Sedentary (little to no exercise)\nEnter 2 for Lightly Active (light exercise/sports 1-3 days a week\nEnter 3 for Moderately Active (moderate exercise/sports 3-5 days a week\nEnter 4 for Very Active (hard exercise/sports 6-7 days a week\nEnter 5 for Extra Active (very hard exercise & physical job or training twice a day: """)
        return self.sex, self.weight, self.height, self.age, self.PAL


    def calculate_results(self):
        if self.sex == "male" or self.sex == "m":
            self.BMR = 88.362 + (13.397 * self.weight) + (4.799 * self.height) - (5.677 * self.age)
        elif self.sex == "female" or self.sex == "f":
            self.BMR = 447.593 + (9.247 * self.weight) + (3.098 * self.height) - (4.330 * self.age)
        else:
            print("Invalid input for sex. Please enter Male/Female or 'm'/'f'.")
            return
        
        if self.PAL == "1":
            self.BMR *= 1.2
        elif self.PAL == "2":
            self.BMR *= 1.4
        elif self.PAL == "3":
            self.BMR *= 1.6
        elif self.PAL == "4":
            self.BMR *= 1.8
        elif self.PAL == "5":
            self.BMR *= 2.0


    

    def show_results(self):
        return "Your total daily calories for one day is " + str(int(self.BMR))

    
print("Welcome to my Total Daily Energy Expenditure calculator")

tdee_calculator = TDEECalculator()

while True:
    tdee_calculator.receive_info()
    tdee_calculator.calculate_results()
    print(tdee_calculator.show_results())

    go_again = input("Do you want to do another? ").lower()
    if go_again == "no" or go_again == "n":
        break
