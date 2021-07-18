import datetime
from Tasks import Task,Pomodoro
x = datetime.datetime(2018, 6, 1)
name="Realizar Atividade Senai"
timeOnTask=10
timeOfInterval=5
numberOfCicles=3
novaTarefa=Task(name,x,timeOnTask,timeOfInterval,numberOfCicles)
novaTarefa.setComplete()
print(novaTarefa.toString())
print("Serão gastos :"+str(novaTarefa.getTotalTime()))

print("Today is :"+x.strftime("%d %B %Y"))

###POMODORO
listaDeTarefas=[novaTarefa,"e","i","o","u"]
pomo=Pomodoro(listaDeTarefas)
#pomo.getAllTasks()
#print(pomo.getTask(0).toString())
pomo.getTask(0).setIncomplete()
#print(pomo.getTask(0).toString())
pomo.insertTask("X")
pomo.getAllTasks()