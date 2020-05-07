usernumber = input("please provide two int number : ")
spltednum = usernumber.split(" ")
num1 = int(spltednum[0])
num2 = int(spltednum[1])



def intg_value(first_value,last_value):
    total_value =(first_value + last_value)

    return total_value

print(intg_value (num1,num2))