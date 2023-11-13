#!/usr/bin/python3
"""
Console module for the command interpreter.
"""
import cmd
import json
from models import storage
from models.base_model import BaseModel
from models.user import User

all_classes = {'BaseModel': BaseModel, 'User': User}}


class HBNBCommand(cmd.Cmd):
    """
    Command interpreter class.
    """

    prompt = '(hbnb) '

    def do_quit(self, arg):
        """
        Quit command to exit the program.
        """
        return True

    def do_EOF(self, arg):
        """
        EOF command to exit the program.
        """
        print()
        return True

    def emptyline(self):
        """
        Do nothing on an empty line.
        """
        pass

    def do_create(self, arg):
        """
        Create a new instance of BaseModel, save it, and print the id.
        """
        if not arg:
            print('** class name missing **')
        else:
            args = arg.split()
            try:
                new_instance = all_classes[args[0]]()
                new_instance.save()
                print(new_instance.id)
            except KeyError:
                print('** class doesn\'t exist **')

    def do_show(self, arg):
        """
        Print the string representation of an instance.
        """
        if not arg:
            print('** class name missing **')
        else:
            args = arg.split()
            class_name = args[0]
            if class_name not in all_classes:
                print('** class doesn\'t exist **')
            elif len(args) == 1:
                print('** instance id missing **')
            else:
                key = "{}.{}".format(class_name, args[1])
                instances = storage.all()
                if key not in instances:
                    print('** no instance found **')
                else:
                    print(instances[key])

    def do_destroy(self, arg):
        """
        Delete an instance based on the class name and id.
        """
        if not arg:
            print('** class name missing **')
        else:
            args = arg.split()
            class_name = args[0]
            if class_name not in all_classes:
                print('** class doesn\'t exist **')
            elif len(args) == 1:
                print('** instance id missing **')
            else:
                key = "{}.{}".format(class_name, args[1])
                instances = storage.all()
                if key not in instances:
                    print('** no instance found **')
                else:
                    del instances[key]
                    storage.save()

    def do_all(self, arg):
        """
        Print all string representations of instances.
        """
        args = arg.split()
        vals = storage.all().values()

        if len(args) < 1:
            print(["{}".format(str(v)) for v in valss])
            return

        if args[0] not in all_classes.keys():
            print('** class doesn\'t exist **')
            return
        else:
            objs = [f"{(str(v)) for v in vals if type(v).__name__ == args[0]}"]
            print(objs)
            return

    def do_update(self, arg):
        """
        Update an instance based on the class name and id.
        """
        if not arg:
            print('** class name missing **')
        else:
            args = arg.split()
            class_name = args[0]
            if class_name not in all_classes:
                print('** class doesn\'t exist **')
            elif len(args) == 1:
                print('** instance id missing **')
            elif "{}.{}".format(class_name, args[1]) not in storage.all():
                print('** no instance found **')
            elif len(args) == 2:
                print('** attribute name missing **')
            elif len(args) == 3:
                print('** value missing **')
            else:
                key = "{}.{}".format(class_name, args[1])
                instance = storage.all()[key]
                attr_name = args[2]
                attr_value = args[3]
                if hasattr(instance, attr_name):
                    attr_type = type(getattr(instance, attr_name))
                    setattr(instance, attr_name, attr_type(attr_value))
                    instance.save()
                else:
                    print('** attribute doesn\'t exist **')


if __name__ == '__main__':
    HBNBCommand().cmdloop()
