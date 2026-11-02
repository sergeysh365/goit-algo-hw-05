The script reads a log file passed as a command-line argument and outputs statistics by log level (e.g., INFO, ERROR, DEBUG). Additionally, the user can specify a log level as a second command-line argument to retrieve all entries for that level.
Example of running a script without an additional argument.

# python main.py path/to/logfile.log

Example of running a script with an additional argument 'error'.

# python main.py path/to/logfile.log error
