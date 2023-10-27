
import os

def rename_nested(folder, suffix, add=True):
    """
    Order to follow to solve the case-sensitive issue:
        1. run the function with add=True
        2. commit the changes
        3. run the function with add=False
        4. commit for the last time

    Args:
        folder (str): the main folder to rename, with the nested as well
        suffix (str): the unique string to add/remove from the path
    """
    amount = 0
    for dirpath, dirnames, filenames in os.walk(folder):
        for d in dirnames:
            complete_dir = os.path.join(dirpath, d)
            if add:
                new_path = complete_dir+suffix
            else:
                new_path = complete_dir.replace(suffix,'')
            os.rename(complete_dir, new_path)
            amount += 1
            amount += rename_nested(new_path, suffix, add)
        break
    return  amount

folder = os.path.dirname(__file__)
suffix = '-----'

# rename_nested(folder, suffix, enum)
amount = rename_nested(folder, suffix, add=False)
print(f'{amount} folders renamed successfully.')
