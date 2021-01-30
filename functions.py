#function to print the first 3 multiples of a number
def first_three_multiples(num):
  print(num)
  print(num * 2)
  third = num * 3
  print(third)
  return third


#calculate the amount to tip based on the total of the food costs and percentage to tip
def tip(total, percentage):
  tip = total * percentage/ 100
  return tip


#return a string of a Bond-style introduction
def introduction(first_name, last_name):
  return (last_name + ", " + first_name + " " + last_name)


#function to take name and and age of dog and return name and age in dog years in appropriate string
def dog_years(name, age):
  age = age * 7
  return name + ", you are " + str(age) + " years old in dog years"


#function to do a lot of mathematical operations
def lots_of_math(a, b, c, d)
  add = a + b
  subtract = c -d
  multiply = add * subtract
  print(str(add))
  print(str(subtract))
  print(str(multiply))
  return multiply % a