import csv


def input_major(*major):
    pass

def input_professor(*professor):
    pass

def input_lesson(*lesson):
    pass

def input_priority(priority):
    pass




filename="전체수강표.csv"
datas=[]
f=open(filename, 'r', encoding='utf-8-sig')
reader=csv.reader(f)
for line in reader:
    datas.append(line)

print(datas)
f.close()
