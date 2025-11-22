
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