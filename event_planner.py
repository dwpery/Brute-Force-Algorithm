import itertools

class Activity:
    def __init__(self, name, time, cost, enjoyment):
        self.name = name
        self.time = time
        self.cost = cost
        self.enjoyment = enjoyment

activities_list = []
time_limit = 0

def process_input_data(filename):
    # Extracts data from input files
    f = open(filename)
    lines = f.readlines()
    f.close()

    # Extracts time limit from file
    constraints = lines[1].strip().split()
    time_limit = int(constraints[0])

    # Converts plain txt into useable objects 
    num_of_activities = int(lines[0].strip())
    for i in range(2, (num_of_activities + 2)):
        attributes = lines[i].strip().split()

        # Creates instance of Activity class and popuilates it with data from input file
        new_activity = Activity(attributes[0], attributes[1], attributes[2], attributes[3])
        activities_list.append(new_activity)
                   
def brute_force_search(activities, time_limit):
    best_combination = []
    best_enjoyment = 0

    for size in range(1, len(activities) + 1):
        for subset in itertools.combinations(activities, size):
            temp_time = 0
            temp_enjoyment = 0

            # Calculates the total time and enjoyment
            for activity in subset:
                temp_time += activity.time
                temp_enjoyment += activity.enjoyment

            # Checks comnination doesnt run over for time
            if temp_time <= time_limit:
                # 
                if temp_enjoyment >= best_enjoyment:
                    best_combination = subset
                    best_enjoyment = temp_enjoyment

    return best_combination, best_enjoyment

if __name__ == "__main__":
    filename = "input_small.txt"