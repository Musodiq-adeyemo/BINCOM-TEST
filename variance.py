# Function to calculate variance of shirts colors
def variance(shirt_colors):
    shirt_list = []
    total = 0
    count = 0
    sum_total = 0
    result = 0
    # Get all values into a list
    for value in shirt_colors.values():
        shirt_list.append(value)
        total += value
        count += 1
        # Calculate mean
        mean = total / count
    # Get the sum of the square of all values minus mean
    for val in shirt_list :
        sum_total += (val - mean)**2
        # Divide sum total by (n-1)
        result = sum_total / (count - 1)
    return result
# Dictionary off shirt colors for the week
shirt_colors = {"Red": 9,"Green":10,"yellow":5,
                "Blew":1,"Brown":6,"Blue":30,
                "Pink":5,"Orange":9,"Cream":2,
                "White":16,"Arsh":1,"Black":1
                }
real_variance = variance(shirt_colors)
print("The Variance of the shirt color is:",real_variance)