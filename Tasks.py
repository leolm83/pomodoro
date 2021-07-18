import datetime
class Task:
    def __init__(self, name,initialDate,timeOnTask,timeOfInterval,numberOfCicles):
        self.name=name
        self.initialDate=initialDate
        self.timeOnTask=timeOnTask
        self.timeOfInterval=timeOfInterval
        self.numberOfCicles=numberOfCicles
        self.totalTime=""
        self.completed=False
    def getTotalTime(self):
        totalTimeMinutes=(self.timeOnTask+self.timeOfInterval)*self.numberOfCicles
        if(totalTimeMinutes>=60):
            hours=totalTimeMinutes/60
            completeHours=int(hours)
            if((totalTimeMinutes-completeHours)>0):
                exceedingMinutes=totalTimeMinutes-(completeHours*60)
                self.totalTime=" {} Hours and {} Minutes ".format(completeHours,exceedingMinutes)
        else:
            self.totalTime=" {} Minutes ".format(totalTimeMinutes)    
        return self.totalTime
    def toString(self):
        return " Task Name :{} \n Start Date : {} \n Time in Activity : {} \n Time of Interval : {} \n Cicles : {} \n Total Time on Task : {} \n Task is complete? {} \n".format(self.name,
        self.initialDate,
        self.timeOnTask,
        self.timeOfInterval,
        self.numberOfCicles,
        self.getTotalTime(),
        self.completed,
        )
    def isComplete(self):
        return self.completed
    def setComplete(self):
        self.completed=True
    def setIncomplete(self):
        self.completed=False
    
class Pomodoro:
    def __init__(self,listOfTasks):
        self.listOfTasks=listOfTasks
    def getAllTasks(self):
        for index,item in enumerate(self.listOfTasks):
            if type(item)==type(""):
                print("Position "+str(index)+" : "+str(item))
            else:
                try:
                    print(item.toString())
                except:
                    print("Infelizmente ocorreu um erro durante a execucao")
    def getTask(self,position):
        #print(self.listOfTasks[position].toString())
        return self.listOfTasks[position]
    def insertTask(self,task):
        self.listOfTasks.append(task)
    

