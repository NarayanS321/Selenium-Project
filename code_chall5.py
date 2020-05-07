user_name1 = input("please provide your name with surname and gendr : ")
splited_name = user_name1.split(" ")
name = splited_name[0]
surname = splited_name[1]
gender = splited_name[2]

def user_name(first_name,last_name,gender):
    total_name = first_name +" " + last_name

    greet = " "

    if gender.lower() == "male":
        greet = "Hello " +"Mr. " + total_name

    elif gender.lower() == "female":
        greet = "Hello " + "MRS " + total_name

    else:
        greet = "Hello" + total_name

    return greet


print(user_name(name,surname,gender))


