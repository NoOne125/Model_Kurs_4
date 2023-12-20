import tabulate as tab
import matplotlib.pyplot as plt

from Create import Create
from Model import Model
from Process import Process
from System import System

T = 70000
k = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
N_repeat = 3
result = []
result2 = []

def run_model(k_list, N_repeat):
    z = 0
    for k in k_list:
        result2.append([])
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
            #c.processes[0].TheorPract()
            #s1.processes[0].TheorPract()
            #s1.processes[1].TheorPract()
            #s2.processes[0].TheorPract()
            #s3.processes[0].TheorPract()
            #s4.processes[0].TheorPract()

            #plt.plot(model.avgfreq_time, model.avgfreq)
            #plt.xlabel("Час прогону")
            #plt.ylabel("Середня відмова")
            #plt.show()
            result2[z].append(N3/N0)
            
            result.append([k, N0 , N1 , N2, N3/N0, G1, G2, G1*N1, G2*N2, G1*N1+G2*N2])
        z+=1

def F():
    avg = 0
    avg_lines =[]
    p = len(k)
    q = N_repeat
    for item1 in result2:
        Sum_line = 0
        for item2 in item1:
            Sum_line+=item2
            avg+=item2
        Sum_line/=q
        avg_lines.append(Sum_line)
    avg/=(p*q)
    S_fact=0
    for item in avg_lines:
        S_fact+=item
    S_fact*=p
    S_zal = 0
    for i in range(p):
        for j in range(q):
            S_zal+=(result2[i][j] - avg_lines[i])*(result2[i][j] - avg_lines[i])
    D_fact = S_fact
    D_zal = S_zal/q/(p-1)
    F = D_fact/D_zal
    print(f"D факт.: {D_fact}")
    print(f"Ступеній свободи.: {q*(p-1)}")
    print(f"D залиш.: {D_zal}")
    print(f"F: {F}")
    return F

        

run_model(k, N_repeat)
F = F()
F_cr = 2.04
print(f"F крит.: {F_cr}")
if(F>F_cr):
    print("Фактор впливу значний")
else:
    print("Фактор впливу не значний")
print (f"Час виконання: {T}\n\n")
print (tab.tabulate(result, headers= ["k", "Пост. повід.", "Перед. Осн.", "Перед. Зап.", "Част. перер.", "Ціна 1 пов. осн.", "Ціна 1 пов. зап.", "Прибут. Осн.", "Приб. Зап.", "Прибуток"]))