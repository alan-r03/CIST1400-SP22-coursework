import csv, math
states = {}

with open('states2020Census.csv', 'r') as csvfile:
    states_reader = csv.reader(csvfile, delimiter=',')

    row_num = 1
    first_row = True
    for row in states_reader:
        if first_row:
            first_row = False
            continue
        print('Row #{}:'.format(row_num), row)
        row_num += 1
        states[row[0]] = {"population": row[1], "priority": float(row[1])/math.sqrt(2), "seats": 1 }open_seats = 435 - (row_num - 1)

while open_seats > 0:
    priority_state = {"state": '', "population": 0, "priority": 0, "seats": 1}
    for key, value in states.items():
        if value["priority"] > priority_state["priority"]:
            priority_state = {"state": key,
                              "population": int(value["population"]),
                              "priority": float(value["priority"]),
                              "seats": int(value["seats"])}

    states[priority_state["state"]] = {"population": priority_state["population"],
                                       "priority": priority_state["population"] / math.sqrt((priority_state["seats"] + 1) * (priority_state["seats"] + 2)),
                                       "seats": priority_state["seats"] + 1}
    open_seats -= 1

print('\n\n')
for state in states:
    print(f"{state:<15} - Population: {states[state]['population']:>8}\t Priority: {states[state]['priority']:>19}\t Seats: {states[state]['seats']:<4}")
    
with open('stateHouseResults2010.txt', 'w') as file:
    for state in states:
        file.write(f"{state}: {states[state]['population']}, {states[state]['priority']}, {states[state]['seats']}\n")

with open('stateHouseResults2010.csv', 'w') as file:
    states_writer = csv.writer(file)
    for state in states:
        states_writer.writerow([state, states[state]["seats"]])
