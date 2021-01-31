#check if a number is within a range
def in_range(num, lower, upper):
  return num >= lower and num <= upper


#check if two strings are the same
def same_name(your_name, my_name):
  return your_name == my_name


#a contradiction 
def always_false(num):
  return num > num


#check range and print appropriate message
def movie_review(rating):
  if rating <= 5:
    return "Avoid at all costs!"
  elif rating < 9:
    return "This one was fun."
  else:
    return "Outstanding!"


#check which of 3 numbers is biggest
def max_num(num1, num2, num3):
  if num1 > num2 and num1 > num3:
    return num1
  elif num2 > num1 and num2 > num3:
    return num2
  elif num3 > num1 and num3 > num2:
    return num3
  else:
    return "It's a tie!"