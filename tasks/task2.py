# tasks/task2.py

def solve():
# Ниже пишите решение задачи

    z,x,c=map(int,input("Введите количество карандашей,ручек,маркеров: ").split())
    karandash=3
    ruchka=karandash+2
    marker=ruchka+7
    vso=(z*karandash)+(x*ruchka)+(c*marker)
    print(vso)
   
# Код ниже не трогать! он нужен для тестов
if __name__ == "__main__":
    solve()