#from __setting__ import *
"""
try:
    import message
except ImportError:
    y = None

if y == None:
    pass
else:
    message.showinfo("Yes!","Yes!")
"""
class CommunicationResult:
    def __init__(self, stdout, stderr, status):
        self.stdout = stdout
        self.stderr = stderr
        self.status = status