# It will give all the information related execution.
# We track errors, customException errors.
# We log any exception into log file.

import logging
import os
from datetime import datetime


LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
# strftime() is a method available for datetime objects that converts a datetime object into a string representation based on a specified format.
# %m: Month as a zero-padded decimal number (e.g., 01 for January, 02 for February).
# %d: Day of the month as a zero-padded decimal number (e.g., 01 to 31).
# %Y: Year with century as a decimal number (e.g., 2022).
# %H: Hour (24-hour clock) as a zero-padded decimal number (e.g., 00 to 23).
# %M: Minute as a zero-padded decimal number (e.g., 00 to 59).
# %S: Second as a zero-padded decimal number (e.g., 00 to 59).

logs_path = os.path.join(os.getcwd(),"logs")

# os.getcwd() returns the current working directory as a string.
# The current working directory is the directory from which the Python script is being executed.
# This is a string representing the name of the directory where log files should be stored.
# It's assumed that there is a directory named "logs" within the current working directory.
# LOG_FILE:This is the filename for the log file, generated using the datetime.now() function as explained earlier.
# logs_path is a variable that holds the full path to the log file. By using os.path.join(), the script constructs the path dynamically, 
# taking into account the current working directory, the "logs" directory, and the filename of the log file. 

os.makedirs(logs_path, exist_ok = True)

# os.makedirs() is a function provided by the os module in Python.
# It creates a directory and any necessary intermediate directories (i.e., parent directories) in the specified path.
# If the directory already exists, os.makedirs() raises an error by default. 
# However, with the exist_ok=True parameter, it will not raise an error if the directory already exists; 
# it will simply ignore the operation.

LOG_FILE_PATH = os.path.join(logs_path,LOG_FILE)

# os.path.join() is a function provided by the os.path module in Python.
# It joins one or more path components together using the appropriate separator for the operating system.
# This function is used to construct file and directory paths in a platform-independent way.
# logs_path is the variable that holds the full path to the directory where log files should be stored.
# LOG_FILE is the filename for the log file, generated earlier using the current date and time.
# LOG_FILE_PATH Assignment:The result of os.path.join(logs_path, LOG_FILE) is assigned to the variable LOG_FILE_PATH.
# It represents the full path to the log file, including the directory path and filename.


logging.basicConfig(
filename = LOG_FILE_PATH,
level = logging.INFO,
format = "[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s"

)

# if __name__ == "__main__":
#     logging.info("Logging has started.")