#pomodoro
#Proxima alteracao em relacao ao caminho HARD CODED para deixa-lo relativo e funcional em qualquer sistema
import time 
from playsound import playsound
tempo_em_tarefa=float(input("Quanto tempo você pretende gastar em cada ciclo na tarefa ?(Tempo na Tarefa Em Cada Ciclo em Minutos) "))
quantidade_ciclos=int(input("Quantos ciclos voce deseja fazer?"))
tempo_descanso=float(input("Quanto tempo você pretende usar para descanso?(Tempo Entre Cada Ciclo Em Minutos) "))
tempo_final=(tempo_em_tarefa+tempo_descanso)*quantidade_ciclos
if tempo_final<1:
    print(f"Serão gastos {tempo_final*60:.1f} Segundos")
else:
    minutos=int(tempo_final)
    segundos=(tempo_final-minutos)*60
    print(f"Serão gastos {minutos} Minutos e {segundos} segundos")
for ciclo in range(quantidade_ciclos):
    print("---- Ciclo "+str(ciclo+1)+" : ----")
    if ciclo!=0:
        print("Volte para tarefa :)")
    else:
        print("Inicie a Tarefa")
    playsound("/home/leolm/LeolmCoding/pomodoro/alarme.mp3")
    time.sleep(tempo_em_tarefa*60)
    playsound("/home/leolm/LeolmCoding/pomodoro/alarme.mp3")
    print("Momento de Descanso!!!")
    time.sleep(tempo_descanso*60)
    print("-----------------------------------")
print("Tarefa encerrada")
