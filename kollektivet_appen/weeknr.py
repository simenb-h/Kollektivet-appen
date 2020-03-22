import datetime

cleaners = ['Simen', 'Stian', 'Sigmund']
tasks = ['gulv', 'bad', 'kjøkken' ]
index = [0,1,2,0,1,2]

def getWeek():
    return datetime.datetime.utcnow().isocalendar()[1] # this week
    #return datetime.date(2020, 3, 31).isocalendar()[1] # two weeks
    #return datetime.date(2020, 3, 24).isocalendar()[1] # one week
    #return datetime.date(2020, 4, 7).isocalendar()[1] # three weeks


def get_index():
    week = getWeek()

    if (week % 3 == 0):
        i = 0
    elif ((week-1) % 3 == 0):
        i = 1
    elif ((week+1) % 3 == 0):
        i = 2
    return i

def getCleaninglist():
    i = get_index()
    thisweek = []     
    en = index[i]
    to = index[i+1]
    tre = index[i+2]
    thisweek = [cleaners[0] + " skal vaske " + tasks[en], cleaners[1] + " skal vaske " + tasks[to], cleaners[2] + " skal vaske " + tasks[tre]]
    return thisweek
