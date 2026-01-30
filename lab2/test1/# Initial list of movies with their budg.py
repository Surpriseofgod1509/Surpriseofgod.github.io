# Initial list of movies with their budgets
movie_list = [
    ("Pirates of the Caribbean: On Stranger Tides", 379000000),
    ("Avengers: Age of Ultron", 365000000),
    ("Avengers: Endgame", 356000000),
    ("Incredibles 2", 200000000)
]

# Step 1: Input Logic
num_movies = int(input("Enter how many new movies you wish to add: "))
for i in range(num_movies):
    name = input("Enter new movie name: ")
    budget = int(input("Enter new movie budget: "))
    movie_list.append((name, budget))

# Step 2: Calculate Average Budget
total_budget = 0
for movie in movie_list:
    total_budget += movie[1]
average_budget = total_budget // len(movie_list)

print(f"\nThe average budget of the movies is: {average_budget}")

# Step 3 & 4: Compare and Output
over_average_count = 0
for movie in movie_list:
    if movie[1] > average_budget:
        difference = movie[1] - average_budget
        print(f"{movie[0]} cost ${movie[1]} : ${difference} over average.")
        over_average_count += 1

print(f"\nThere were {over_average_count} movies with over average budgets.")
