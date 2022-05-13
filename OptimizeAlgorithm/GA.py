
import pandas as pd
import random
import copy
import time
from datetime import datetime, date, timedelta


class Tasks:
    def __init__(self, id, name, arrival_time, deadline, estimated_time, flexible=1):
        self.id = id
        self.name = name
        self.arrival_time = arrival_time
        self.deadline = deadline
        self.estimated_time = estimated_time
        self.flexible = flexible

# total_fixed_time = 0
# for fft in filter_fixed_time :
#     total_fixed_time += minutes_between_two_date(later_date = (fft['to_time']),first_date=(fft['from_time']))
# print(minutes_between_two_date(later_date = toDate(recommended_schedule_to),first_date=toDate(recommended_schedule_from)) - total_fixed_time)

# Sinh cá thể trong quần thể

def on_generation(break_time, tasks, recommended_schedule_from, recommended_schedule_to):
    fixed_time = break_time
    minDistance = 15
    fixed_time.append({'from_time': toDate(recommended_schedule_from), 'to_time': toDate(recommended_schedule_from)})
    fixed_time.append({'from_time': toDate(recommended_schedule_to), 'to_time': toDate(recommended_schedule_to)})

    for task in tasks:
        if task['flexible'] == 0:
            fixed_time.append(
                {'from_time': task['arrival_time'], 'to_time': task['deadline']})
    fixed_time.sort(key=lambda x: x['from_time'])

    filter_fixed_time = [fixed_time[0]]
    for i in range(1, len(fixed_time)):
        if(int((fixed_time[i]['from_time'] - filter_fixed_time[-1]['to_time']).total_seconds() / 60) <= minDistance):
            filter_fixed_time[-1]['to_time'] = fixed_time[i]['to_time']
        else:
            filter_fixed_time.append(fixed_time[i])

    flexible_task_ids = []
    for task in tasks:
        if task['flexible'] == 1:
            flexible_task_ids.append(task['id'])

    population = []
    num_individual = 5
    for i in range(num_individual):
        random.shuffle(flexible_task_ids)
        population.append({'individual_id': i, 'flexible_task_ids': flexible_task_ids[:]})
        individual_schedule = set_individual_schedule(flexible_task_ids=population[i]['flexible_task_ids'], filter_fixed_time=copy.deepcopy(filter_fixed_time), tasks=tasks)
        population[i]['individual_schedule'] = individual_schedule
        
    return population

def set_individual_schedule(flexible_task_ids, filter_fixed_time, tasks):
    individual_schedule = []
    filter_fixed_time_index = 0
    flexible_tasks=[]
    for j in flexible_task_ids :
        for task in tasks :
            if (task['id']==j):
                flexible_tasks.append(task)
    for task in flexible_tasks :
        task['remaining_time'] = task['estimated_time']
        while task['remaining_time'] > 0 :
            x = minutes_between_two_date(later_date = filter_fixed_time[filter_fixed_time_index+ 1]['from_time'], first_date = filter_fixed_time[filter_fixed_time_index]['to_time'])
            if task['remaining_time'] < x:
                individual_schedule.append({
                    'id': task['id'],
                    'start_time': filter_fixed_time[filter_fixed_time_index]['to_time'],
                    'duration': task['remaining_time'],
                    'remaining_time': 0
                    })
                filter_fixed_time[filter_fixed_time_index]['to_time'] += timedelta(minutes=(task['remaining_time']))
                task['remaining_time'] = 0

            elif task['remaining_time'] == x:
                individual_schedule.append({
                    'id': task['id'],
                    'start_time': filter_fixed_time[filter_fixed_time_index]['to_time'],
                    'duration': task['remaining_time'],
                    'remaining_time': 0
                    })
                task['remaining_time'] = 0
                filter_fixed_time_index = filter_fixed_time_index + 1
            else:
                individual_schedule.append({
                    'id': task['id'],
                    'start_time': filter_fixed_time[filter_fixed_time_index]['to_time'],
                    'duration': x,
                    'remaining_time': task['remaining_time'] - x
                    })
                task['remaining_time'] = task['remaining_time'] - x
                filter_fixed_time_index = filter_fixed_time_index + 1
    # printListObject(individual_schedule)
    # print('_______')
    return individual_schedule

def minutes_between_two_date(later_date, first_date):
    duration = later_date - first_date
    duration_in_s = duration.total_seconds()
    minutes = divmod(duration_in_s, 60)[0]
    return minutes


def fitness_func(individual_schedule, flexible_task_ids, tasks):
    flexible_tasks=[]
    for j in flexible_task_ids :
        for task in tasks :
            if (task['id']==j):
                flexible_tasks.append(task)
    schedule_lateness = 0
    for schedule in individual_schedule:
        if schedule['remaining_time'] == 0:
            for task in flexible_tasks:
                if task['id'] == schedule['id'] :
                    if (schedule['start_time'] + timedelta(minutes=(schedule['duration']))) > task['deadline']:
                        task['lateness'] = minutes_between_two_date((schedule['start_time'] + timedelta(minutes=(schedule['duration']))), task['deadline'])
                    else:
                        task['lateness'] = 0
                    schedule_lateness += task['lateness']
    # print(schedule_lateness)
    # print(flexible_task_ids)
    return schedule_lateness

def on_selection(population):
    selected_population = population
    selected_population.sort(key=lambda x: x['lateness'])
    temp = {}
    for p in selected_population:
        temp[p['lateness']] = p
    selected_population = list(temp.values())
    return selected_population[:2]

def on_crossover(parents):
    flexible_task_ids = parents[0]['flexible_task_ids']
    parents_1 = parents[0]['flexible_task_ids']
    parents_2 = parents[1]['flexible_task_ids']
    temp_child_1 = []
    temp_child_2 = []
    child_1 = []
    child_2 = []
    # print(random.randint(2,len(flexible_task_ids))  )
    while ( temp_child_1 == temp_child_2):
        temp_child_1 = []
        temp_child_2 = []
        x = random.randint(2,(len(flexible_task_ids)-1))  
        crossover_items = random.sample(parents[0]['flexible_task_ids'],x)
        for id in parents_1:
            if id in crossover_items:
                temp_child_1.append(id)
        for id in parents_2:
            if id in crossover_items:
                temp_child_2.append(id)
    i = 0
    for p in parents_1:
        if p in temp_child_1:
            child_1.append(temp_child_2[i])
            i+=1
        else:
            child_1.append(p)
    j = 0
    for p in parents_2:
        if p in temp_child_2:
            child_2.append(temp_child_1[j])
            j+=1
        else:
            child_2.append(p)
    return child_1, child_2

def toDate(datetime_str):
    return datetime.strptime(datetime_str, '%Y-%m-%d %H:%M:%S')

def printListObject(listObject):
    for item in listObject:
        print(item)

def main():
    start = time.time()
    recommended_schedule_from = '2021-11-15 08:00:00'
    recommended_schedule_to = '2021-11-19 17:00:00'
    tasks = pd.read_excel(r'tasks.xlsx').to_dict('records')
    break_time = pd.read_excel(r'breakTime.xlsx').to_dict('records')
    population = on_generation(break_time=break_time, tasks=tasks, recommended_schedule_from=recommended_schedule_from,
                  recommended_schedule_to=recommended_schedule_to)
    for i in range(len(population)):
        population[i]['lateness'] = fitness_func(individual_schedule = population[i]['individual_schedule'], flexible_task_ids = population[i]['flexible_task_ids'], tasks=tasks)
    
    two_best_individuals = on_selection(population)
    # print(two_best_individuals)
    x= on_crossover(parents = two_best_individuals)
    # print(x, "crossover")
    end = time.time()
    print(end-start)

if __name__ == '__main__':
    main()
    # test()
