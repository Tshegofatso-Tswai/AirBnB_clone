# AirBnB_clone
This project is a command interpreter for an AirBnB clone. It allows the user to create, read, update and delete objects representing places to stay, as well as handle reservations and customer information.

# Command Interpreter
The command interpreter is a command line interface (CLI) that allows the user to interact with the program by typing in commands. It is written in Python and uses object-oriented programming principles.

# How to start the Command Interpreter
To start the command interpreter, you can navigate to the root directory of the project in the terminal and run the command -> python3 console.py <- which will the command interpreter

# How to use the command iinterpreter
Once the command interpreter is running, you can use the following commands:

create <class>: creates a new instance of the class and saves it to a JSON file.
show <class> <id>: prints the string representation of the instance with the given id.
all: prints all string representations of all instances.
update <class> <id> <attribute> <value>: updates the attribute of the instance with the given id.
destroy <class> <id>: deletes the instance with the given id.
quit: exits the command interpreter.

# Examples (3)
1. To create a new instance of the class Place, type: (hbnb) create Place
2. To show the string representation of an instance of class Place with id 123, type: (hbnb) show Place 123
3. To update the attribute name of an instance of class Place with id 123, type:(hbnb) update Place 123 name "New Name"
