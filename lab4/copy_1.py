import os

def copy_self(target_directory, file_count):
    # Get the path of the current script
    current_script = os.path.abspath(__file__)

    # Read the contents of the current script
    with open(current_script, 'r') as f:
        script_content = f.read()

    # Create specified number of files and copy the script content into them
    for i in range(file_count):
        file_path = os.path.join(target_directory, f'copy_{i+1}.py')

        # Write the script content to the new file
        with open(file_path, 'w') as target_file:
            target_file.write(script_content)

if __name__ == "__main__":
    # Specify the target directory
    target_directory = "./lab4"
    
    # Specify the number of files to create
    file_count = 1

    # Ensure the target directory exists
    if not os.path.exists(target_directory):
        os.makedirs(target_directory)

    # Call the function to copy the script to new files
    copy_self(target_directory, file_count)
