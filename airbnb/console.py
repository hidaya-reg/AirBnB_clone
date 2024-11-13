#!/usr/bin/python3
"""the entry point of the command interpreter"""
import cmd
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    """Command Interpreter"""

    prompt = "(hbnb) "
    classes = {
        "BaseModel": BaseModel,
        "User": User,
        "Place": Place,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Review": Review
    }

    def do_quit(self, arg):
        """Exit the command interpreter"""
        return True
    
    def do_EOF(self, arg):
        """Exit the command interpreter on EOF"""
        return True
    
    def do_help(self, arg):
        """Display help information"""
        super().do_help(arg)
    
    def emptyline(self):
        """Do nothing on empty line"""
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel"""
        if not arg:
            print("** class name missing **")
            return
        
        class_name = arg
        cls = globals().get(class_name)

        if not cls:
            print("** class doesn't exist **")
            return

        instance = cls()
        storage.new(instance)
        storage.save()
        print(instance.id)

    def do_show(self, arg):
        """prints the sting representation of an instance
        based on the class name and id
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in globals():
            print("** class doesn't exist **")
            return
        
        if len(args) < 2:
            print("** instance id missing **")
            return
        
        instance_id = args[1]
        instances = storage.all()
        key = f"{class_name}.{instance_id}"
        if key in instances:
            print(instances[key])
        else:
            print("** no instance found **")
        
    def do_destroy(self, arg):
        """Deletes an instance based on class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in globals():
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        key = f"{class_name}.{instance_id}"
        instances = storage.all()
        if key not in instances:
            print("** no instance found **")
        else:
            del instances[key]
            storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances
        based or not on the class name"""
        instances = storage.all()
        if not arg:
            print([str(obj) for obj in instances.values()])
            return
        
        class_name = arg
        cls = globals().get(class_name)

        if not cls:
            print("** class doesn't exist **")
            return
        
        print([str(instances[k]) for k in instances.keys() if k.startswith(class_name + ".")])

    def do_update(self, arg):
        if not arg:
            print("** class name missing **")
            return
        
        args = arg.split()
        class_name = args[0]
        cls = globals().get(class_name)

        if not cls:
            print("** class doesn't exist **")
            return
        
        if len(args) < 2:
            print("** instance id missing **")
            return
        
        instance_id = args[1]
        instances = storage.all()
        key = f"{class_name}.{instance_id}"
        if key not in instances:
            print("** no instance found **")
            return
        instance = instances[key]
        if len(args) < 3:
            print("** attribute name missing **")
            return
        
        attr_name = args[2]
        
        if len(args) < 4:
            print("** value missing **")
            return
        
        attr_value = " ".join(args[3:]).strip('"')

        current_value = getattr(instance, attr_name, None)
        if isinstance(current_value, int):
            attr_value = int(attr_value)
        elif isinstance(current_value, float):
            attr_value = float(attr_value)

        # Set the attribute and save the instance
        setattr(instance, attr_name, attr_value)
        storage.save()

    def do_count(self, class_name):
        """Counts the instances of a specific class"""
        count = sum(1 for key in storage.all() if key.startswith(class_name))
        print(count)

    def default(self, line):
        """Handle commands of the form <class name>.all() and <class name>.count()"""
        args = line.split(".")
        if len(args) == 2:
            class_name, command = args
            if class_name in self.classes:
                if command.startswith("show(") and command.endswith(")"):
                    instance_id = command[5:-1]  # Extract the ID from show(<id>)
                    self.do_show(f"{class_name} {instance_id}")
                elif command.startswith("destroy(") and command.endswith(")"):
                    instance_id = command[8:-1]  # Extract the ID from show(<id>)
                    self.do_destroy(f"{class_name} {instance_id}")
                elif command.startswith("update(") and command.endswith(")"):
                    instance_data = command[7:-1]  # Extract arguments for update
                    self.do_update(instance_data)
                elif command == "all()":
                    self.do_all(class_name)
                elif command == "count()":
                    self.do_count(class_name)
                else:
                    print("*** Unknown syntax:", line)
            else:
                print("** class doesn't exist **")
        else:
            print("*** Unknown syntax:", line)

if __name__ == "__main__":
    HBNBCommand().cmdloop()
