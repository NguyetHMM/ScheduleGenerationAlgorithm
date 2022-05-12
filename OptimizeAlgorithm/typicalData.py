from datetime import datetime, date

typicalData = {
    'startTime': '2021-11-15 08:00:00',
    'endTime': '2021-11-19 17:00:00',
    'timeNotUsed': [
        {
            'fromTime':'2021-11-15 12:00:00',
            'toTime':'2021-11-15 13:00:00'
        },
        {
            'fromTime':'2021-11-16 12:00:00',
            'toTime':'2021-11-16 13:00:00'
        },
        {
            'fromTime':'2021-11-17 12:00:00',
            'toTime':'2021-11-17 13:00:00'
        },
        {
            'fromTime':'2021-11-18 12:00:00',
            'toTime':'2021-11-18 13:00:00'
        },
        {
            'fromTime':'2021-11-19 12:00:00',
            'toTime':'2021-11-19 13:00:00'
        },
        {
            'fromTime':'2021-11-15 17:00:00',
            'toTime':'2021-11-15 20:00:00'
        },
        {
            'fromTime':'2021-11-16 17:00:00',
            'toTime':'2021-11-16 20:00:00'
        },
        {
            'fromTime':'2021-11-17 17:00:00',
            'toTime':'2021-11-17 20:00:00'
        },
        {
            'fromTime':'2021-11-18 17:00:00',
            'toTime':'2021-11-18 20:00:00'
        },
        {
            'fromTime':'2021-11-15 23:00:00',
            'toTime':'2021-11-16 08:00:00'
        },
        {
            'fromTime':'2021-11-16 23:00:00',
            'toTime':'2021-11-17 08:00:00'
        },
        {
            'fromTime':'2021-11-17 23:00:00',
            'toTime':'2021-11-18 08:00:00'
        },
        {
            'fromTime':'2021-11-18 23:00:00',
            'toTime':'2021-11-19 08:00:00'
        }
    ],
    'tasks':[
            {
            'taskId': 12,
            'name': 'Nhật NetK',
            'startTime': '2021-11-15 18:00:00',
            'endTime': '2021-11-15 20:00:00',  # deadline
            'estimatedTime': '120',
            'flexible': 0,
        },
        {
            'taskId': 1,
            'name': 'Nhật NetK',
            'startTime': '2021-11-17 18:00:00',
            'endTime': '2021-11-17 20:00:00',  # deadline
            'estimatedTime': '120',
            'flexible': 0,
        },
        {
            'taskId': 2,
            'name': 'Nhật NetK',
            'startTime': '2021-11-18 18:00:00',
            'endTime': '2021-11-18 20:00:00',  # deadline
            'estimatedTime': '120',
            'flexible': 0,
        },
        {
            'taskId': 3,
            'name': 'Mạng Internet',
            'startTime': '2021-11-16 06:45:00',
            'endTime': '2021-11-16 08:15:00',  # deadline
            'estimatedTime': '90',
            'flexible': 0,
        },
        {
            'taskId': 4,
            'name': 'ITSS 2',
            'startTime': '2021-11-16 08:25:00',
            'endTime': '2021-11-16 11:45:00',  # deadline
            'estimatedTime': '200',
            'flexible': 0,
        },
        {
            'taskId': 5,
            'name': 'Realtime System',
            'startTime': '2021-11-17 06:45:00',
            'endTime': '2021-11-17 08:15:00',  # deadline
            'estimatedTime': '90',
            'flexible': 0,
        },
        {
            'taskId': 6,
            'name': 'Knowledge Engineering',
            'startTime': '2021-11-17 10:15:00',
            'endTime': '2021-11-17 11:45:00',  # deadline
            'estimatedTime': '90',
            'flexible': 0,
        },
        {
            'taskId': 7,
            'name': 'Họp ITSS',
            'startTime': '2021-11-15 21:00:00',
            'endTime': '2021-11-15 23:00:00',  # deadline
            'estimatedTime': '120',
            'flexible': 0,
        },
        {
            'taskId': 8,
            'name': 'Script ITSS',
            'startTime': '2021-11-15 08:00:00',
            'endTime': '2021-11-15 21:00:00',  # deadline
            # 'estimatedTime': '60-120',
            'estimatedTime': '60',
            'flexible': 1,
        },
        {
            'taskId': 9,
            'name': 'Ôn tập Realtime System',
            'startTime': '2021-11-15 08:00:00',
            'endTime': '2021-11-17 06:45:00',  # deadline
            # 'estimatedTime': '300-480',
            'estimatedTime': '480',
            'flexible': 1,
        },
        {
            'taskId': 10,
            'name': 'Thuật toán GR',
            'startTime': '2021-11-15 08:00:00',
            'endTime': '2021-11-19 17:00:00',  # deadline
            'estimatedTime': '960',
            'flexible': 1,
        },
        {
            'taskId': 11,
            'name': 'Knowledge Engineering Project',
            'startTime': '2021-11-15 08:00:00',
            'endTime': '2021-11-19 17:00:00',  # deadline
            'estimatedTime': '660',
            'flexible': 1,
        }
    ],
    'passSchedule':{
        'user_email': "hmn@gmail.com",
        'schedule': [
        {
            'task_id': 1,
            'start_time': "",
            'executed_time': 2
        },
        {
            'task_id': 2,
            'start_time': "",
            'executed_time': 2
        }, 
        {
            'task_id': 3,
            'start_time': "",
            'executed_time': 2
        }, 
        {
            'task_id': 4,
            'start_time': "",
            'executed_time': 2
        }, 
        {
            'task_id': 5,
            'start_time': "",
            'executed_time': 2
        }, 
        {
            'task_id': 6,
            'start_time': "",
            'executed_time': 2
        }, 
        {
            'task_id': 7,
            'start_time': "",
            'executed_time': 2
        },
        {
            'task_id': 8,
            'start_time': "",
            'executed_time': 2
        },
        {
            'task_id': 9,
            'start_time': "",
            'executed_time': 2
        },
        {
            'task_id': 10,
            'start_time': "",
            'executed_time': 2
        }
    ]}
    }

def toDate(datetime_str) :
    return datetime.strptime(datetime_str, '%Y-%m-%d %H:%M:%S')

def differenceBetweenToDate(laterDate, firstDate) :

    # laterDate = toDate(laterDateStr)
    # firstDate = toDate(firstDate)
    duration = laterDate - firstDate
    duration_in_s = duration.total_seconds()
    minutes = divmod(duration_in_s, 60)[0] 
    return minutes

def getAvaiableTime(startTime, endTime, timeNotUsed, tasks) : 
    totalTimeNotUsed = 0
    timeForFixedTasks = 0

    for timeNotUsedElement in timeNotUsed :
        toTime = toDate(timeNotUsedElement.get('toTime'))
        fromTime = toDate(timeNotUsedElement.get('fromTime'))
        totalTimeNotUsed += differenceBetweenToDate( laterDate = toTime, firstDate = fromTime)

    for task in tasks:
        if task.get('flexible') == 0 :
            taskEndTime = toDate(task.get('endTime'))
            taskStartTime = toDate(task.get('startTime'))
            timeForFixedTasks += differenceBetweenToDate( laterDate = taskEndTime, firstDate = taskStartTime)
    
    print(timeForFixedTasks)
    
    avaiableTime = differenceBetweenToDate( laterDate=toDate(endTime), firstDate=toDate(startTime)) - totalTimeNotUsed - timeForFixedTasks
        
    return avaiableTime

startTime = typicalData.get('startTime')
endTime = typicalData.get('endTime')
timeNotUsed=typicalData.get('timeNotUsed')
tasks=typicalData.get('tasks')

# print(getAvaiableTime(startTime=startTime, endTime=endTime, timeNotUsed=timeNotUsed, tasks=tasks),"avaiable time")
avaiableTime = getAvaiableTime(startTime=startTime, endTime=endTime, timeNotUsed=timeNotUsed, tasks=tasks)
# print(tasks)

def preProcessData(tasks):
    inputTasksData = []
    for item in tasks:
        if item['flexible'] == 1:
            print(item)
            itemStartTime = toDate(item.get('startTime'))
            itemEndTime = toDate(item.get('endTime'))
            # itemArrivalTime = toDate(typicalData.get('startTime'))
            itemDeadline = differenceBetweenToDate( laterDate = itemEndTime, firstDate = toDate(startTime))
            itemArrivalTime = differenceBetweenToDate( laterDate = itemStartTime, firstDate = toDate(startTime))
            inputTasksData.append([item['taskId'], int(item['estimatedTime']), avaiableTime, itemDeadline, itemArrivalTime])
    print (inputTasksData, "inputData")

    # return inputTasksData

def suggestScheduling():
    suggestedScheduling = []
    passScheduling =  typicalData.get('passSchedule').get('schedule')
    if(len(passScheduling)!=0):
        Get

    return suggestedScheduling

if __name__ == "__main__" : 
  
    preProcessData(tasks)

