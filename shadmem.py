#!/usr/bin/env python3

import sys
import time
import cmd
import re
from shadmemory import ShadSharedMemory
from spimanager import SPIManager

__version__ = '2017.07.04'

class ShadMemApp(cmd.Cmd):
    """This is the aplication class."""

    def __init__(self):
        cmd.Cmd.__init__(self)
        self.prompt_counter = 0
        self.RefreshPrompt()
        self.sharedmem = ShadSharedMemory(None,True)
        self.spiman    = SPIManager()
        self._matchComment = re.compile(r'\s*[#].*')

    def __exit__(self,exc_type,exc_value,traceback):
        """Nada por enquanto."""
        pass

    def __enter__(self):
        return self

    def __str__(self):
        """Return info about the current instance."""
        return "ShadMemApp"

    def do_do(self,args):
        """Low leval commands - use only for debugging!"""
        self.spiman.do('ACTION',args)

    def do_sendmsg(self,args):
        """Send a little messsage"""
        print(args)

    def do_quit(self,args):
        """Leaves the application""" 
        print("Thank you for playing!")
        return True

    def do_exit(self,args):
        """Leaves the application""" 
        return self.do_quit(args)

    def do_comment(self,args):
        """Comments"""
        pass

    def precmd(self,line):
        match = self._matchComment.search(line)
        if match != None:
            line = "comment"
        return cmd.Cmd.precmd(self,line)

    def postcmd(self,stop,line):
        self.RefreshPrompt()
        return cmd.Cmd.postcmd(self,stop,line)
        
    def preloop(self):
        self.sharedmem.open()

    def postloop(self):
        self.sharedmem.close()
        print('*bye*')
        self.RefreshPrompt()

    def RefreshPrompt(self):
        self.prompt_counter += 1
        cmd.Cmd.prompt = str(self.prompt_counter)+'++ '
        
def main(argv=None):
    if argv is None:
        argv = sys.argv

    try:
        with ShadMemApp() as app:
            app.cmdloop()
    except ValueError as e:
        print('[-] ',e)
        sys.exit(1)

    return 0

if __name__ == "__main__":
    sys,exit(main())

