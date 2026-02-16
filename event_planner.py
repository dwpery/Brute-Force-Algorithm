import itertools
import time

class Activity:
    def __init__(self, name, time, cost, enjoyment):
        self.name = name
        self.time = int(time)
        self.cost = int(cost)
        self.enjoyment = int(enjoyment)

activities_list = []
time_limit = 0
budget_limit = 0

def process_input_data(filename):
    # Extracts data from input files
    f = open(filename)
    lines = f.readlines()
    f.close()

    # Extracts time limit from file
    constraints = lines[1].strip().split()
    time_limit = int(constraints[0])
    budget_limit = int(constraints[1])

    # Converts plain txt into useable objects 
    num_of_activities = int(lines[0].strip())
    for i in range(2, (num_of_activities + 2)):
        attributes = lines[i].strip().split()

        # Creates instance of Activity class and popuilates it with data from input file
        new_activity = Activity(attributes[0], attributes[1], attributes[2], attributes[3])
        activities_list.append(new_activity)

    return activities_list, time_limit, budget_limit
                   
def brute_force_search(activities, time_limit):
    best_combination = []
    best_enjoyment = 0

    # Evaluates every possible subset to find best combination
    for size in range(1, len(activities) + 1):
        for subset in itertools.combinations(activities, size):
            temp_time = 0
            temp_enjoyment = 0

            # Calculates the total time and enjoyment
            for activity in subset:
                temp_time += activity.time
                temp_enjoyment += activity.enjoyment

            # Finds a best combo that doesnt run over time and has high enjoyment
            if temp_time <= time_limit and temp_enjoyment >= best_enjoyment:
                    best_combination = subset
                    best_enjoyment = temp_enjoyment

    return best_combination, best_enjoyment

if __name__ == "__main__":
    # Extracts data from chosen input file
    filename = "input_large.txt"
    activities_list, time_limit, budget_limit = process_input_data(filename)

    # Performs brute force and calculates execution time
    start_time = time.time()
    best_combination, best_enjoyment = brute_force_search(activities_list, time_limit)
    end_time = time.time()
    execution_time = end_time - start_time

    print("========================================")
    print("EVENT PLANNER - RESULTS")
    print("========================================")

    print(f"\nInput File: {filename}")
    print(f"Available Time: {time_limit}")
    print(f"Available Budget: {budget_limit}")

    print(f"\n--- Brute Force Algorithm ---\nSelected Activities:")

    # Prints the result of the brute force search and totals attributes so they can be printed
    total_time = 0
    total_cost = 0
    total_enjoyment = 0
    for activity in best_combination:
        print(f"- {activity.name} ({activity.time} hours, £{activity.cost}, enjoyment {activity.enjoyment})")
        total_time += activity.time
        total_cost += activity.cost
        total_enjoyment += activity.enjoyment

    print(f"Total Enjoyment: {total_enjoyment}")
    print(f"Total Time Used: {total_time}")
    print(f"Total Cost: {total_cost}")

    print(f"\nExecution Time: {execution_time} seconds")