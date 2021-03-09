import numpy as np

# Calculate the probability that the student knows the material given that they answered correctly

p_knows_material = 0.6
p_correct_given_knows = 0.85
p_anyone_correct = (0.6 * 0.85) + (0.4 * 0.2)

p_knows_given_correct = (0.85 * 0.6) / p_anyone_correct
print (p_knows_given_correct)
