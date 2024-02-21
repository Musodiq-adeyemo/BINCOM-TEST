# Function to get the probability of color red
def prob_of_red(shirt_colors):
    total = 0
    red_count = 0
    # Get total values
    for value in shirt_colors.values():
        total += value
    # Get value of red
    red_count = shirt_colors.get("Red",0)
    if red_count == 0:
        return 0     
    else:
         # Divide value of red by total value
        result = red_count / total   
        return result
#Dictionary of shirt colors
shirt_colors = {"Red": 9,"Green":10,"yellow":5,
                "Blew":1,"Brown":6,"Blue":30,
                "Pink":5,"Orange":9,"Cream":2,
                "White":16,"Arsh":1,"Black":1
                }
probability_of_red = prob_of_red(shirt_colors)
print("The probability of getting a color red is:",probability_of_red)