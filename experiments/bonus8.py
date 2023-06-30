date = input("Enter today date: ")
mood = input("Rate your mood from 1 to 10: ")
thoughts = input("Thoughts:\n")

with open(f"../journal/{date}.txt", 'ww') as file:
    file.write(mood + 2 * '/n')
    file.write(thoughts)