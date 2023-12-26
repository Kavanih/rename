
# #WITH numbers
import os

folder_path = r'C:\Users\Mohd\Documents\omnes\Assets'  # Use 'r' to denote a raw string
counter = 0

for filename in os.listdir(folder_path):
    if filename.endswith('.png'):
        new_name = f'{counter}.png'
        os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, new_name))
        counter += 1

print("File renaming completed with sequential numbers.")



# WITH Aphabets
# import os
# import random
# import string

# folder_path = r'C:\Users\Mohd\Documents\omnes\Assets'  # Use 'r' to denote a raw string

# def generate_random_filename(length=4):
#     alphanumeric_chars = string.digits + string.ascii_lowercase
#     return ''.join(random.choice(alphanumeric_chars) for _ in range(length))

# for filename in os.listdir(folder_path):
#     if filename.endswith('.png'):
#         file_extension = os.path.splitext(filename)[1]
#         new_name = generate_random_filename() + file_extension
        
#         while os.path.exists(os.path.join(folder_path, new_name)):
#             # Ensure the new name doesn't already exist in the directory
#             new_name = generate_random_filename() + file_extension

#         # Rename the file
#         os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, new_name))

# print("File renaming completed with shuffled names.")

