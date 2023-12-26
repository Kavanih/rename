
#WITH numbers
import os

folder_path = r'file pathe'  # Use 'r' to denote a raw string
counter = 4429

for filename in os.listdir(folder_path):
    if filename.endswith('.png'):
        new_name = f'{counter:04d}.png'  # Rename to 4-digit zero-padded numbers with .png extension
        os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, new_name))
        counter += 1



# WITH Aphabets
import os

folder_path = r'file pathe'  # Use 'r' to denote a raw string
counter = 0
alphabet = 'abcdefghijklmnopqrstuvwxyz'

for filename in os.listdir(folder_path):
    if filename.endswith('.png'):
        if counter < len(alphabet):
            new_name = f'{alphabet[counter]}.png'  # Rename using alphabet characters with .png extension
            os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, new_name))
            counter += 1
        else:
            print("Ran out of alphabet characters. You can add more if needed.")
            break
