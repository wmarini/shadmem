"""SPI Manager class and functions."""

class SPIManager(object):
    """SPI Manager Class"""

    verbos = ['COMMENT','ACTION','COMMAND','SETTER']

    def __init__(self):
        self._command = None

    def do(self,ctx,cmd):
        self._command = cmd
        if ctx == 'COMMENT':
            return
        if ctx == 'ACTION':
            print('action: '+ctx,cmd['action'])
        elif ctx == 'COMMAND':
            print('command: '+ctx,cmd['command'])
        elif ctx == 'SETTER':
            print('setter: '+ctx,cmd)
        else:
            prin('[-] undefined')
