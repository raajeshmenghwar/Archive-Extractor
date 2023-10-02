#!/usr/bin/python3
print('*#'*50)
print("\t\t\t[+] Programmed by rKumar ")
print("\t\t\t[+] Commented  by ChatGPT")
print('*#'*50)    
# Import necessary libraries
import zipfile
import tarfile
from py7zr import SevenZipFile
import magic
from rarfile import RarFile
import os  # Import the os module for file existence checks

while True:
    try:
        # Create a Magic object to determine the type of the compressed file
        magic_obj = magic.Magic()

        # Prompt the user to enter the compressed file's path
        userInput = input("[+] Enter the compressed file to extract it (or 'q' to quit): ")
        
        # Check if the user wants to quit
        if userInput.lower() == 'q':
            break

        # Check if the specified file exists
        if not os.path.exists(userInput):
            print("[+] File not found:", userInput)
            continue

        # Use the Magic object to identify the file type
        fileType = magic_obj.from_file(userInput)

        # Check if the file is a Zip archive
        if 'Zip' in fileType:
            # Create a ZipFile object for the specified zip file
            zip_file = zipfile.ZipFile(userInput)

            # Extract all the contents of the zip file to the current working directory
            zip_file.extractall()

            # Close the ZipFile object
            zip_file.close()
            print("[+] " + userInput+" extracted successfully ...")

        # Check if the file is a tar archive
        elif 'tar' in fileType:
            tarfile_obj = tarfile.TarFile(userInput)

            # Extract all the contents of the tar file to the current working directory
            tarfile_obj.extractall()

            # Close the TarFile object
            tarfile_obj.close()
            print("[+] " + userInput+" extracted successfully ...")

        # Check if the file is a 7-Zip archive
        elif '7-zip' in fileType:
            SevenZipFile_obj = SevenZipFile(userInput)
            
            # Extract all the contents of the 7-Zip file to the current working directory
            SevenZipFile_obj.extractall()
            
            # Close the SevenZipFile object
            SevenZipFile_obj.close()
            print("[+] " + userInput+" extracted successfully ...")

        # Check if the file is a RAR archive
        elif 'rar' in fileType:
            rarfile_obj = RarFile(userInput)
            
            # Extract all the contents of the RAR file to the current working directory
            rarfile_obj.extractall()
            
            # Close the RarFile object
            rarfile_obj.close()
            print("[+] " + userInput+" extracted successfully ...")

        else:
            # Print an error message if the file type is not supported
            print("[+] File type: " + fileType + " cannot be extracted here ...")
    except FileNotFoundError as e:
        print("[+] Sorry, " + userInput + " not found:", e)
    except Exception as e:
        print("[+] An error occurred while processing " + userInput + ":", e)
