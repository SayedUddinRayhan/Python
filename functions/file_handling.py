
# file = open('functions/text_file.txt', 'r')
# content = file.read()
# print(content)
# file.close()

# Most used way to handle file
with open("functions/text_file.txt", 'r') as file:
    content = file.read()
    print(content)

# Writing to a file
# with open("functions/text_file.txt", 'w') as file:
#     file.write("\nHello , This is text File") 
# 'w' mode will overwrite the existing content

# Appending to a file
with open("functions/text_file.txt", 'a') as file:
    file.write("\nThis line is appended.")


# List
my_list = ['\napple', '\nbanana', '\ncherry']

with open("functions/text_file.txt", 'a') as file:
    file.writelines(my_list)



import os 

if os.path.exists("functions/text_file.txt"):
    print("The file exists.")
else:
    print("The file does not exist.")

# Path
print("Absolute Path:", os.path.abspath("functions/text_file.txt"))
print("Directory Name:",  os.path.dirname(os.path.abspath("functions/text_file.txt")))
# Size
print("File Size in bytes:", os.path.getsize("functions/text_file.txt"))