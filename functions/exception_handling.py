
# Error vs Exception
# Error: A serious problem that a program should not try to catch. (Syntax Error, Indentation Error)
# Exception: An event that occurs during the execution of a program that disrupts the normal flow of instructions.

# Exception --> Run time Error

# try: # je code e exception ashte pare shei code ke try block e rakhte hoy
#     with open("functions/text_file.txt", 'r') as file:
#         content = file.read()
#         print(content)
#     # print(10 / 0)  # This will raise a ZeroDivisionError
#     # print(int("abc"))  # This will raise a ValueError
#     # i = [1, 2, 3]
#     # print(i[100])  # This will raise an IndexError
#     # x = abc  # This will raise a NameError
# # except FileNotFoundError: # specific exception handle korte chaile
# #     print("Error: The file was not found.")

# except FileNotFoundError as e: # specific exception handle korte chaile
#     print("Error: The file was not found.", e)

# except ZeroDivisionError:
#     print("Error: Division by zero is not allowed.")

# except ValueError:
#     print("Error: Invalid value.")

# except IndexError:
#     print("Error: Index out of range.")

# except Exception as e: # general exception handle korte chaile
#     print("An error occurred:", e)

# else: # jokhon try block e kono exception ashe na tokhon else block run hoy
#     print("File read successfully without any errors.")
# finally: # finally block always run hoy, exception asuk na asuk
#     print("Execution completed.")

# Ami nije exception baniyechi
# def check_file(filename):
#     if not filename.endswith('.png'):
#         raise ValueError("Invalid file type. Only .png files are allowed.")
#     print("File is valid.")

# check_file("text.txt")  # This will raise a ValueError


def file_upload(filename):
    try:
        if not filename.endswith('.png'):
            raise ValueError("Invalid file type. Only .png files are allowed.")
        print("File uploaded successfully.")
    except ValueError as ve:
        print("File upload failed:", ve)

file_upload("image.jpg")  # This will raise a ValueError