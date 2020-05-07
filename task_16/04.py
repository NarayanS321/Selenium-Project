"""
a,b = 6,11
c,d = 12,1
e,f = 2,4
g,h = 5, 9
i,j = 10,12
"""

name = input("What is your name : ")
time1 = input("what is the current time : ")
time1_spletied = time1.split(",")
#print("time1_spletied")
time_in_int = int(time1_spletied[0])
am_pm = time1_spletied[1]
#print(time1_spletied[0])
#print(time1_spletied[1])

if (time_in_int >= 5) and (time_in_int <= 11):
    print("Good morning " + name)
elif (time_in_int >= 12) and (time_in_int <= 1):
    print("Good Noon " +name)
elif (time_in_int >= 2) and (time_in_int <= 4):
    print("Good evng " +name)
elif (time_in_int >= 5) and (time_in_int <= 9):
    print("Good night " +name)

else:
    print("Go to Bed " +name)


