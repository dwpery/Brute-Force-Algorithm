import intertools

class Activity:
    def __init__(self, name, time, cost, enjoyment):
        self.name = name
        self.time = time
        self.cost = cost
        self.enjoyment = enjoyment

activities_list = []

def process_input_data(filename):
    # Extracts data from input files
    f = open(filename)
    lines = f.readlines()
    f.close()

    # Converts plain txt into useable objects 
    num_of_activities = int(lines[0].strip())
    for i in range(2, (num_of_activities + 2)):
        attributes = lines[i].strip().split()

        # Creates instance of Activity class and popuilates it with data from input file
        new_activity = Activity(attributes[0], attributes[1], attributes[2], attributes[3])
        activities_list.append(new_activity)
                   
def brute_force_search(activities, time_limit):
    best_combination = []
    highest_enjoyment = 0

    for size in range(1, len(activities) + 1):


# def results