#!/user/bin/python2
# -*- coding: utf-8 -*-

# size_position.py

import wx

class Example(wx.Frame):

    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title, size=(250, 200))

        self.Show()

if __name__ == "__main__":
    
    app = wx.App()
    Example(None, title='size')
    app.MainLoop()
