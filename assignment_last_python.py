# #Assignment 1
# #Create an assignment for File handling of JSON files in Python

# # sloution 1
# import json


# class Employee:
#     def __init__(self, name, dob, height, city, state):
#         self.name = name
#         self.dob = dob
#         self.height = height
#         self.city = city
#         self.state = state


# def read_employee_data_from_json(filename):
#     employee_list = []
#     with open(filename, 'r') as file:
#         data = json.load(file)
#         for emp_data in data['employees']:
#             name = emp_data['Name']
#             dob = emp_data['DOB']
#             height = emp_data['Height']
#             city = emp_data['City']
#             state = emp_data['State']
#             employee = Employee(name, dob, height, city, state)
#             employee_list.append(employee)
#     return employee_list


# if __name__ == '__main__':
#     file_name = 'employee.json'
#     employees = read_employee_data_from_json(file_name)


#     for emp in employees:
#         print(f"Name: {emp.name}, DOB: {emp.dob}, Height: {emp.height}, City: {emp.city}, State: {emp.state}")


# #solution 2
# # Create a dictionary of any 7 Indian states and their capitals and write it into a JSON file

# indian_states_capitals = {
#     "Maharashtra": "Mumbai",
#     "Karnataka": "Bengaluru",
#     "Tamil Nadu": "Chennai",
#     "Delhi": "New Delhi",
#     "Uttar Pradesh": "Lucknow",
#     "Rajasthan": "Jaipur",
#     "Gujarat": "Gandhinagar"
# }

# import json
# with open('C:/Users/user/Music/indian_states_capitals.json', 'w') as file:
#     json.dump(indian_states_capitals, file)



# Assignment 2
# Create a class named ‘Dog’. It should have a constructor which accepts its name, age and coat color. 
# You must perform the following operation


class Dog:
    def __init__(self, name, age, coat_color):
        self.name = name 
        self.age = age 
        self.coat_color = coat_color

    def description(self):
        print(f"{self.name} is {self.age} years old.")
    def get_info(self):
        print(f"The coat color of {self.name} is {self.coat_color}.")

class JackRussellTerrier(Dog):
    def __init__(self, name, age, coat_color, special_skill):
        super().__init__(name, age, coat_color)
        self.special_skill = special_skill


    def description(self):
        super().description()
        print(f"{self.name} has a special skill: {self.special_skill}.")

class Bulldog(Dog):
    def __init__(self, name, age, coat_color,weight):
        super().__init__(name, age, coat_color)
        self.weight = weight

    def description(self):
        super().description()
        print(f"{self.name} is a Bulldog.")

    def get_info(self):
        super().get_info()
        print(f"{self.name} weights {self.weight} kg.") 

if __name__ == '__main__':
    dog1 = Dog("Buddy", 5, "Brown")

    dog1.description()
    dog1.get_info()

    print("\n")

    dog2 = JackRussellTerrier("Rocky", 3, "White and Brown", "Digging")
    dog2.description()
    dog2.get_info()
    print("\n")

    dog3 = Bulldog("Max", 4, "White", 25)
    dog3.description()
    dog3.get_info()

