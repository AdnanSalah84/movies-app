# "r" - Read - Default value. Opens a file for reading, error if the file does not exist
#
# "a" - Append - Opens a file for appending, creates the file if it does not exist
#
# "w" - Write - Opens a file for writing, creates the file if it does not exist
#
# "x" - Create - Creates the specified file, returns an error if the file exists

file_handle = None

try:
    print("The TRY block attempts to run")
    # t means this is a text file (otherwise it would specify b for a binary file)
    file_handle = open('spam1.txt', 'xt')
    file_handle.write('Spam, spam, spam!\n')
except FileNotFoundError as error:
    print("This CATCH block only runs if this error happens")
    print(f"The following file can not be found: {error.filename}. Please try another file")
except FileExistsError as error:
    print("This CATCH block only runs if this error happens")
    print(f"The following file already exists: {error.filename}.")
except Exception as err:
    print("Generic except / catch block")
    print(err)
finally:
    # Always close file handle after use
    print("The FINALLY block ALWAYS runs")
    if file_handle is not None:
        print("Make sure you don't cause an exception to occur in the Finally block")
        file_handle.close()


print("After exception handling is finished")


