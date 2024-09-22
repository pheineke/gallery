import os
import re

def clean_filename(filename):
    # Separate the filename and the extension
    name, ext = os.path.splitext(filename)

    # Use regex to replace non-alphanumeric characters except spaces, underscores, or dots
    clean_name = re.sub(r'[^\w\s._-]', '', name)

    # Return the cleaned name with the original extension
    return clean_name + ext

def rename_files_in_directory(directory):
    # Get a list of all files in the directory
    for filename in os.listdir(directory):
        # Create the full path of the current file
        old_path = os.path.join(directory, filename)
        
        # Skip directories and focus only on files
        if os.path.isfile(old_path):
            # Clean the filename
            new_filename = clean_filename(filename)
            
            # If the new filename is different, rename the file
            if new_filename != filename:
                new_path = os.path.join(directory, new_filename)
                os.rename(old_path, new_path)
                print(f'Renamed: "{filename}" to "{new_filename}"')

if __name__ == '__main__':
    # Path to the folder containing files
    directory_path = './static/media/'
    
    # Call the renaming function
    rename_files_in_directory(directory_path)
