#Function to calculate the mean color of shirt worn
def mean(shirt_colors):
    total = 0
    count = 0
    # Iterate over all the values in our shirt colors dictionary using for loop
    for frequency in shirt_colors.values():
        total += frequency
        count += 1
        # our mean is total numbers of colors for all the days divided by number of colors
        result = total / count
    return result
# A dictionary containing the colors and their respective numbers
shirt_colors = {"Red": 9,"green":10,"yellow":5,
                "Blew":1,"Brown":6,"Blue":30,
                "Pink":5,"Orange":9,"Cream":2,
                "White":16,"Arsh":1,"Black":1
                }
real_mean = mean(shirt_colors)
# Print the mean of the shirt colors
print("The mean of the shirt color is:",real_mean)
