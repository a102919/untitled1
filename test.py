def getData(file):
    my_file = open(file, 'r')
    content = my_file.read()
    allData = []
    for data in content.split('\n'):
        allData.append(data.split((', ')))
    return allData

def create_C1(data_set):
    C1 = set()
    for t in data_set:
        for item in t:
            item_set = frozenset([item])
            C1.add(item_set)
    return C1

def creat_L1(C1,allData):
    L1 = {}
    for all in allData:
        for c in C1:
            if c.issubset(all):
                if c in L1 :
                    L1[c] += 1
                else:
                    L1[c] = 1

    return L1


def getNewLk(L1):
    Lk = set()
    for item in L1:
        if L1[item] >= SUP:
            Lk.add(item)
    return Lk


def getCk(Lk,run):
    newCk = set()
    ListLk = list(Lk)
    Lksize = len(Lk)
    for i in range(Lksize):
        for j in range(i + 1, Lksize):
            list1 = list(ListLk[i])
            list2 = list(ListLk[j])
            list1.sort()
            list2.sort()
            if list1[0:run - 2] == list2[0:run - 2]:
                orItem = ListLk[i] | ListLk[j]
                if checkIncloud(orItem,Lk):
                    newCk.add(orItem)
    return newCk

def checkIncloud(orItem,Lk):
    for item in orItem:
        i = orItem - frozenset([item])
        if i not in Lk:
            return False
        return True


if __name__ == "__main__":
    file = 'file\\T15I7N0.5KD1K.txt'
    frq = 0
    SUP = 5
    allData = getData(file)
    newCk = create_C1(allData)
    L1 = creat_L1(newCk,allData)

    NewLk = getNewLk(L1)
    frq += len(NewLk)
    while len(newCk) >= 1:
        run = 2
        newCk = getCk(NewLk,run) #製造新的Ck
        countCk = creat_L1(newCk,allData) #計算數量
        NewLk = getNewLk(countCk) #將低於的值排除
        print(NewLk)
        frq += len(NewLk)
        run += 1

print(frq)



