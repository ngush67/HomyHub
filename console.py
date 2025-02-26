#!/usr/bin/python3

"""console Module """

import cmd

class HomyHubCommand(cmd.Cmd):
    """Command interpreter for HomyHub"""
    
    prompt = "(HomyHub) "

    def do_quit(self, arg):
        """Exit the program"""
        return True

    def do_EOF(self, arg):
        """Handle EOF (Ctrl+D) to exit"""
        print("")
        return True

    def emptyline(self):
        """Ignore empty lines"""
        pass

if __name__ == "__main__":
    HomyHubCommand().cmdloop()
