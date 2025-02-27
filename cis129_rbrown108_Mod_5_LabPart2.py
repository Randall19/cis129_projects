"""This program illustrates a count controlled loop that repeats a specified number of times.
I will use a while loop and increment a counter.  When the counterexceeds the conditional limit,
the while loop value will become 'False' and the loop will terminate.
cis129_Brittany_Griwzow  Author Randall Brown rbrown108"""
#declare variables
todayBottles= 0
totalPayout = 0
countDay = 1
depRate = .10
totalBottles = 0
keepGoing = 'y'
weekCounter = 0
while keepGoing:
    while countDay < 8:
        todayBottles=int(input(f'Please enter the number of bottles returned for day number {countDay:>2}\n'))
        print('collection day no ', countDay, ' today bottles ', todayBottles )
        totalBottles += todayBottles
        print('running total of bottles collected is ',  totalBottles)
        countDay += 1
    totalPayout = totalBottles*depRate
    print(f'The payout for this 7 day collection of bottles for deposits was ${totalPayout:.2f}')
    weekCounter += 1
    print('Data entry is done for bottle collection for week ', weekCounter)
    totalPayout=0
    countDay = 1
    totalBottles = 0
    todayBottles = 0
    workMore= input('Do you want to enter data for another week of bottle collections? enter y for yes or n for no ')                         
    if workMore == 'y':
        keepGoing == 'y'
        print('the keep going flag is ', bool(keepGoing))
        print('Let\'s enter data for another week.')
    else:
        print('Bottle deposit data entry is complete.')
        keepGoing = ''
        print('the keep going flag is ', bool(keepGoing))
                         
