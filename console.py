#!/usr/bin/python3
"""console module for HBNB command interpreter """

import cmd
from models.base_model import BaseModel
from models import storage
import shlex

class HBNBCommand(cmd.Cmd):
    """Command interpreter for the HBNB project."""

    prompt = "(hbnb) "
    classes = {"BaseModel": BaseModel}

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """Handles EOF (Ctrl+D) to exit the program."""
        print("")
        return True

    def emptyline(self):
        """Do nothing when an empty line is entered."""
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it, and prints the id."""
        if not arg:
            print("** class name missing **")
            return
        if arg not in self.classes:
            print("** class doesn't exist **")
            return
        obj = self.classes[arg]()
        obj.save()
        print(obj.id)

    def do_show(self, arg):
        """Prints the string representation of an instance based on class name and id."""
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
            return
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = f"{args[0]}.{args[1]}"
        all_objs = storage.all()
        if key not in all_objs:
            print("** no instance found **")
            return
        print(all_objs[key])

    def do_destroy(self, arg):
        """Deletes an instance based on class name and id."""
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
            return
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = f"{args[0]}.{args[1]}"
        all_objs = storage.all()
        if key not in all_objs:
            print("** no instance found **")
            return
        del all_objs[key]
        storage.save()

    def do_all(self, arg):
        """Prints all instances of a class or all instances if no class is specified."""
        all_objs = storage.all()
        if arg:
            if arg not in self.classes:
                print("** class doesn't exist **")
                return
            print([str(obj) for key, obj in all_objs.items() if key.startswith(arg)])
        else:
            print([str(obj) for obj in all_objs.values()])

    def do_update(self, arg):
        """Updates an instance based on class name and id."""
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
            return
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = f"{args[0]}.{args[1]}"
        all_objs = storage.all()
        if key not in all_objs:
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return

        obj = all_objs[key]
        attr_name = args[2]
        attr_value = args[3]

        try:
            if hasattr(obj, attr_name):
                attr_type = type(getattr(obj, attr_name))
                attr_value = attr_type(attr_value)
            else:
                attr_value = eval(attr_value)
        except (ValueError, NameError, SyntaxError):
            pass

        setattr(obj, attr_name, attr_value)
        obj.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()

