class Activity:
    def __init__(self, name, time, cost, enjoyment):
        self.name = name
        self.time = time
        self.cost = cost
        self.enjoyment = enjoyment

activities_list = []

def process_input_data(filename):
    f = open(filename)
    lines = f.readlines()

    f.close()

# def brute_force_search: