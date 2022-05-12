class Tasks:
  def __init__(self, id, name, arrivalTime, deadline, estimatedTime, flexible = 1 ):
    self.id = id
    self.name = name
    self.arrivalTime = arrivalTime
    self.deadline = deadline
    self.estimatedTime = estimatedTime
    self.flexible = flexible

def dataValidate(recommendedScheduleFrom, recommendedScheduleTo, tasks):
    # if recommendedScheduleFrom
    return 1