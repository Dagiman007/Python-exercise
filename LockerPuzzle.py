
def main():
    locker_status = [False] * 100

    l = changeLockerStatus(locker_status)
    open_lockers = openLockers(locker_status)

    print('Number of open lockers is ', len(open_lockers),'. They are \n')
    for i in range(len(open_lockers)):
        print(open_lockers[i], end = ' ')

def changeLockerStatus(locker_status):
    for i in range(100):
        for j in range(i, 100, i + 1):
            if locker_status[j] == True:
                locker_status[j] = False
            else:
                locker_status[j] = True

def openLockers(locker_status):
    indexOfOpenLockers = []
    for i in range(len(locker_status)):
        if locker_status[i] == True:
            indexOfOpenLockers.append(i)

    return indexOfOpenLockers

main()
