# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.richtext

ID_NEW = 1000
ID_OPEN = 1001
ID_SAVE = 1002
ID_EXIT = 1003
ID_ABOUT = 1004

###########################################################################
## Class MyFrame
###########################################################################

class MyFrame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"記事本", pos = wx.DefaultPosition, size = wx.Size( 511,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		self.menu_bar = wx.MenuBar( 0 )
		self.Files = wx.Menu()
		self.menu_new = wx.MenuItem( self.Files, ID_NEW, u"建立檔案"+ u"\t" + u"ctrl+n", wx.EmptyString, wx.ITEM_NORMAL )
		self.Files.Append( self.menu_new )

		self.menu_open = wx.MenuItem( self.Files, ID_OPEN, u"開啟舊案"+ u"\t" + u"crtl+o", wx.EmptyString, wx.ITEM_NORMAL )
		self.Files.Append( self.menu_open )

		self.menu_save = wx.MenuItem( self.Files, ID_SAVE, u"儲存檔案"+ u"\t" + u"ctrl+s", wx.EmptyString, wx.ITEM_NORMAL )
		self.Files.Append( self.menu_save )

		self.Files.AppendSeparator()

		self.menu_exit = wx.MenuItem( self.Files, ID_EXIT, u"關閉程式"+ u"\t" + u"esc", wx.EmptyString, wx.ITEM_NORMAL )
		self.Files.Append( self.menu_exit )

		self.menu_bar.Append( self.Files, u"檔案" )

		self.About = wx.Menu()
		self.menu_about = wx.MenuItem( self.About, ID_ABOUT, u"關於作者", wx.EmptyString, wx.ITEM_NORMAL )
		self.About.Append( self.menu_about )

		self.menu_bar.Append( self.About, u"關於" )

		self.SetMenuBar( self.menu_bar )

		layout = wx.BoxSizer( wx.VERTICAL )

		self.my_rich_text = wx.richtext.RichTextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0|wx.VSCROLL|wx.HSCROLL|wx.NO_BORDER|wx.WANTS_CHARS )
		layout.Add( self.my_rich_text, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( layout )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_MENU, self.new, id = self.menu_new.GetId() )
		self.Bind( wx.EVT_MENU, self.open, id = self.menu_open.GetId() )
		self.Bind( wx.EVT_MENU, self.save, id = self.menu_save.GetId() )
		self.Bind( wx.EVT_MENU, self.exit, id = self.menu_exit.GetId() )
		self.Bind( wx.EVT_MENU, self.about, id = self.menu_about.GetId() )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def new( self, event ):
		event.Skip()

	def open( self, event ):
		event.Skip()

	def save( self, event ):
		event.Skip()

	def exit( self, event ):
		event.Skip()

	def about( self, event ):
		event.Skip()


