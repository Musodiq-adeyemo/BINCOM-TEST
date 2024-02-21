# Function to calculate the shirt colors middle number
def median(shirt_colors):
    # Create an empty list of colors
    color_list = []
    # Iterate over the dictionary values and append all values
    for value in shirt_colors.values():
        color_list.append(value)
        # Sort out the appended value
        sorted_color = sorted(color_list)
        color_len = len(sorted_color)
    # calculate the median 
    middle_number  = color_len // 2
    return ((sorted_color[middle_number] + sorted_color[~middle_number]) / 2.0)
 # Dictionary of shirt colors   
shirt_colors = {"Red": 9,"green":10,"yellow":5,
                "Blew":1,"Brown":6,"Blue":30,
                "Pink":5,"Orange":9,"Cream":2,
                "White":16,"Arsh":1,"Black":1
                }
real_median = median(shirt_colors)
print("The median of the shirt color is:",real_median)

    