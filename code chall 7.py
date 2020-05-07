usernumber = input("please provide two int number : ")
spltednum = usernumber.split(" ")
num1 = int(spltednum[0])
num2 = int(spltednum[1])



def subt_value(first_value,last_value):

    total_value = " "
    if first_value > last_value:
        total_value = (first_value - last_value)
    else :
         total_value = (last_value - first_value)


    return total_value

print(subt_value(num1,num2))

