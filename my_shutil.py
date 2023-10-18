import os
import shutil

if __name__ == "__main__":
    folder_name = "folder_zip"
    zip_name = "my_zip.zip"

    # Create a folder and three files inside it
    os.mkdir(folder_name)
    with open(os.path.join(folder_name, "file1.txt"), "w") as file1:
        file1.write("This is file 1")
    with open(os.path.join(folder_name, "file2.txt"), "w") as file2:
        file2.write("This is file 2")
    with open(os.path.join(folder_name, "file3.txt"), "w") as file3:
        file3.write("This is file 3")

    # Archive folder contents into a zip file
    shutil.make_archive(zip_name, 'zip', folder_name)

    # Copy the zip file to one folder above the current directory
    destination_folder = os.path.join(os.getcwd(), os.pardir)
    shutil.copy(zip_name + ".zip", destination_folder)

    # Remove the folder from disk
    shutil.rmtree(folder_name)

    # Prompt the user to check the folder state
    response = input("Check the folder state. Do you want to extract the archive? (y/n): ")

    # Unpack the archive in the current folder
    if response.lower() == "y":
        shutil.unpack_archive(zip_name + ".zip", folder_name)

    # Print the disk usage of the folder where the archive was copied
    folder_path = os.path.join(destination_folder, zip_name + ".zip")
    usage = shutil.disk_usage(folder_path)
    print(f"Disk Usage for {folder_path}: Total={usage.total}, Free={usage.free}, Used={usage.used}")
