'''user_input = input("please enter a name with extension like .dot ,.jpj ,.mp3 ,.py : ")
user_input1 = user_input.split(".")
name = user_input1[0]
extension = user_input1[1]
print(name)
print(extension)
'''
#user_input = input("please enter a name with extension like .dot ,.jpj ,.mp3 ,.py : ")

"""
def user_input(a):
    if user_input(a).split("."):
        
     return user_input(a) 
        
        
 print(user_input)
"""

def getExtension(filename):
    filename_splitted = filename.split(".") # ["Greetings", "jpg"]
    filename_part = filename_splitted[0]
    extension_part = filename_splitted[1]
    full_extension = "." + extension_part

    return full_extension