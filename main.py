# variables
viriable = 24
units = "hours"


def days_to_units(num_of_days):
  return f"{num_of_days} days are {num_of_days * viriable} {units} "


# my_var = days_to_units(20)
# print(my_var)

user_input = input("Hey, enter a number of days and I will covert in to hours!\n")
user_number = int(user_input)
calculated_value = days_to_units(user_number)
print(calculated_value)



# def scope_check(num_of_days):
  #  my_var1 = "Variable inside fuction"
   # print(units)
   # print(num_of_days)
   # print(my_var1)



# scope_check(23)

# days_to_units(60, "How is the calculations")
# days_to_units(60, "Look good!")



# case 1
# print("20 days are " + str(50) + " seconds ")

# case 2
# print(f"20 days are {20 * viriable } {units} ")
# print(f"35 days are { 35  * viriable } {units} ")
# print(f"100 days are { 100 * viriable } {units} ")
# print(f"180 days are { 180 * viriable  } {units} ")

