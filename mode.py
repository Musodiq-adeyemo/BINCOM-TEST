# Function to find the mostly worn color throughout the week
def mode(shirt_colors):
    highest = 0
    shirt_list = []
    # Arrange the values in a list
    for value in shirt_colors.values():
        shirt_list.append(value)
    # Get the highest value 
    for num in shirt_list:
        if num >= highest :
            highest = num
    # Get the key of the highest value
    for key,val in shirt_colors.items():
        if val == highest:
            return (key,val)
    
# Dictionary of the shirt colors
shirt_colors = {"Red": 9,"green":10,"yellow":5,
                "Blew":1,"Brown":6,"Blue":30,
                "Pink":5,"Orange":9,"Cream":2,
                "White":16,"Arsh":1,"Black":1
                }
real_mode =mode(shirt_colors)
print("The mode of the shirt color is:",real_mode)