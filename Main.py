import tabulate as tab

from Create import Create
from Model import Model
from Process import Process
from System import System

T = 10000
k = [0,5,20,60,100]
N_repeat = 3
result = []

def run_model(k_list, N_repeat):
    for k in k_list:
        for i in range(N_repeat):
            G1 = 50-0.03*k
            G2 = 25 - 0.03*k
            c = System([Create("Creator",9,5)],0,0)
            s1 = System([Process("Основний канал",7,3),Process("Запасний канал",7,3)],0,float('inf'))
            s2 = System([Process("Виникнення збою",200 + k,35)],1,1)
            s3 = System([Process("Ввімкнення запасного каналу", 2,0)],0,0)
            s4 = System([Process("Виправлення збою", 70, 7)],0,0)
            c.processes[0].nextElement = s1
            s1.processes[1].state = -1
            s2.processes[0].nextElement = s3
            s3.processes[0].nextElement = s4
            s4.processes[0].nextElement = s2
            s2.processes[0].Block = True
            s3.processes[0].Block = True
            s2.processes[0].itemBlock = s1.processes[0]
            s4.processes[0].itemBlock = s1.processes[1]
            s1.processes[0].nextElementBlock = s1
            s2.Active()
            systems = [c,s1,s2,s3,s4]
            model = Model(systems)
            model.simulate(T)
            N0 = c.processes[0].quantity
            N1 = s1.processes[0].quantity
            N2 = s1.processes[1].quantity
            N3 = s1.processes[0].quantBlock
            result.append([k, N0 , N1 , N2, N3/N0, G1, G2, G1*N1, G2*N2, G1*N1+G2*N2])

run_model(k, N_repeat)
print (f"Час виконання: {T}\n\n")
print (tab.tabulate(result, headers= ["k", "Пост. повід.", "Перед. Осн.", "Перед. Зап.", "Част. перер.", "Ціна 1 пов. осн.", "Ціна 1 пов. зап.", "Прибут. Осн.", "Приб. Зап.", "Прибуток"]))