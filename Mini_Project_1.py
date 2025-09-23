#Fake News Headline Generator

import random

# Lists of words to create fake news headlines
subjects = ["Scientists", "Politicians", "Celebrities", "Teachers", "Doctors"]
verbs = ["discover", "ban", "promote", "criticize", "support"]
objects = ["new technology", "controversial law", "health trend", "education reform", "climate change initiative"]
adjectives = ["shocking", "unexpected", "controversial", "groundbreaking", "alarming"]
places = ["in the US", "worldwide", "in Europe", "in Asia", "locally"]
times = ["today", "this week", "this month", "recently", "last year"]

while True:
    # Generate a random headline
    headline = f"{random.choice(subjects)} {random.choice(verbs)} {random.choice(adjectives)} {random.choice(objects)} {random.choice(places)} {random.choice(times)}."
    
    # Print the generated headline
    print(headline)
    
    # Ask the user if they want to generate another headline
    again = input("Generate another headline? (yes/no): ").strip().lower()
    if again != 'yes':
        break           
print("Thank you for using the Fake News Headline Generator!")      
