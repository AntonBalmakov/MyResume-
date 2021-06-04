d= {
    1:'one',
    2:'two',
    3:'three',
    4:'four',
}
# for key in d:
#    print(key,d[key])
c ={}
a = 'Anton Balmakov 1996 10 10 8 10'
a = a.split()
c['name'] = a[0]
c['lasname'] = a[1]
c['age'] = a[2]
c['count'] = []

for i in a[3:]:
    c['count'].append(int(i))
# print(c)


class open_file:
    def __init__(self,filename,mode):
        self.f = open(filename,mode)

    def __enter__(self):
        return self.f

    def __exit__(self, *args):
        self.f.close()
import time


def dec(fn):
    def wrap():
        print("Начинаю оборачивать , подожните 3 секунды")
        time.sleep(3)
        fn()
        print("я обернул")
        time.sleep(3)
        print("Пытаюсь выйти с цикла")
        time.sleep(2)
        print('я смооог')
    return wrap

@dec
def show():
    print("я толстая функция , оберни меня")

# show()
tt=[]
a = [1,3,56,7,8,6,45,4,90]
for i in a:
    if i > 5:
        tt.append(i)

# print(tt)

gg = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
bb = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
result = list(filter(lambda elem: elem in gg, bb))
print(result)
