# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"MemberSysteM(MSM)", pos = wx.DefaultPosition, size = wx.Size( 800,420 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.Size( 800,420 ) )
		self.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_TELETYPE, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		gbSizer1 = wx.GridBagSizer( 0, 0 )
		gbSizer1.SetFlexibleDirection( wx.BOTH )
		gbSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.m_button1 = wx.Button( self, wx.ID_ANY, u"新增(不要輸入編號)", wx.DefaultPosition, wx.Size( 110,50 ), 0 )
		self.m_button1.SetFont( wx.Font( 8, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "新細明體" ) )

		bSizer1.Add( self.m_button1, 0, wx.ALL, 5 )

		self.m_button5 = wx.Button( self, wx.ID_ANY, u"更改", wx.DefaultPosition, wx.Size( 110,50 ), 0 )
		bSizer1.Add( self.m_button5, 0, wx.ALL, 5 )

		self.m_button6 = wx.Button( self, wx.ID_ANY, u"刪除", wx.DefaultPosition, wx.Size( 110,50 ), 0 )
		bSizer1.Add( self.m_button6, 0, wx.ALL, 5 )

		self.m_button7 = wx.Button( self, wx.ID_ANY, u"顯示清單", wx.DefaultPosition, wx.Size( 110,50 ), 0 )
		bSizer1.Add( self.m_button7, 0, wx.ALL, 5 )

		self.m_button10 = wx.Button( self, wx.ID_ANY, u"電話系統", wx.DefaultPosition, wx.Size( 110,50 ), 0 )
		bSizer1.Add( self.m_button10, 0, wx.ALL, 5 )

		self.m_button8 = wx.Button( self, wx.ID_ANY, u"離開系統", wx.DefaultPosition, wx.Size( 110,50 ), 0 )
		bSizer1.Add( self.m_button8, 0, wx.ALL, 5 )


		gbSizer1.Add( bSizer1, wx.GBPosition( 0, 2 ), wx.GBSpan( 1, 1 ), 0, 5 )

		bSizer2 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"姓         名", wx.Point( -1,-1 ), wx.Size( -1,-1 ), 0 )
		self.m_staticText3.Wrap( -1 )

		self.m_staticText3.SetFont( wx.Font( 16, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "新細明體" ) )

		bSizer2.Add( self.m_staticText3, 0, wx.ALL, 10 )

		self.m_textCtrl5 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,30 ), 0 )
		bSizer2.Add( self.m_textCtrl5, 0, wx.ALL, 5 )

		self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, u"西元  出生年月日", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )

		self.m_staticText6.SetFont( wx.Font( 10, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "新細明體" ) )

		bSizer2.Add( self.m_staticText6, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )

		self.m_textCtrl6 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,30 ), 0 )
		bSizer2.Add( self.m_textCtrl6, 0, wx.ALL, 5 )

		self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, u"地           址", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )

		self.m_staticText7.SetFont( wx.Font( 16, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "新細明體" ) )

		bSizer2.Add( self.m_staticText7, 0, wx.ALL, 5 )

		self.m_textCtrl7 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,30 ), 0 )
		bSizer2.Add( self.m_textCtrl7, 0, wx.ALL, 5 )

		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"會員   編號", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )

		self.m_staticText4.SetFont( wx.Font( 16, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "新細明體" ) )

		bSizer2.Add( self.m_staticText4, 0, wx.ALL, 5 )

		self.m_textCtrl8 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,30 ), 0 )
		bSizer2.Add( self.m_textCtrl8, 0, wx.ALL, 5 )


		gbSizer1.Add( bSizer2, wx.GBPosition( 0, 3 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )

		bSizer6 = wx.BoxSizer( wx.VERTICAL )

		self.m_textCtrl30 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 520,350 ), wx.TE_DONTWRAP|wx.TE_MULTILINE|wx.TE_PROCESS_ENTER )
		self.m_textCtrl30.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_TELETYPE, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer6.Add( self.m_textCtrl30, 0, wx.ALL, 5 )


		gbSizer1.Add( bSizer6, wx.GBPosition( 0, 4 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )


		self.SetSizer( gbSizer1 )
		self.Layout()
		self.m_statusBar1 = self.CreateStatusBar( 1, wx.STB_SIZEGRIP, wx.ID_ANY )

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button1.Bind( wx.EVT_BUTTON, self.create_add )
		self.m_button5.Bind( wx.EVT_BUTTON, self.create_change )
		self.m_button6.Bind( wx.EVT_BUTTON, self.create_delete )
		self.m_button7.Bind( wx.EVT_BUTTON, self.create_show )
		self.m_button10.Bind( wx.EVT_BUTTON, self.create_tel )
		self.m_button8.Bind( wx.EVT_BUTTON, self.create_close )
		self.m_textCtrl5.Bind( wx.EVT_TEXT_ENTER, self.text1 )
		self.m_textCtrl6.Bind( wx.EVT_TEXT_ENTER, self.text2 )
		self.m_textCtrl7.Bind( wx.EVT_TEXT, self.text3 )
		self.m_textCtrl8.Bind( wx.EVT_TEXT, self.text5 )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def create_add( self, event ):
		event.Skip()

	def create_change( self, event ):
		event.Skip()

	def create_delete( self, event ):
		event.Skip()

	def create_show( self, event ):
		event.Skip()

	def create_tel( self, event ):
		event.Skip()

	def create_close( self, event ):
		event.Skip()

	def text1( self, event ):
		event.Skip()

	def text2( self, event ):
		event.Skip()

	def text3( self, event ):
		event.Skip()

	def text5( self, event ):
		event.Skip()


###########################################################################
## Class TelSystem
###########################################################################

class TelSystem ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"電話系統", pos = wx.DefaultPosition, size = wx.Size( 447,350 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.Size( 447,350 ) )

		sbSizer1 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, wx.EmptyString ), wx.VERTICAL )

		bSizer3 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText15 = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"請選擇會員編號:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText15.Wrap( -1 )

		self.m_staticText15.SetFont( wx.Font( 10, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "新細明體" ) )

		bSizer3.Add( self.m_staticText15, 0, wx.ALL, 5 )

		self.m_textCtrl15 = wx.TextCtrl( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 120,30 ), 0 )
		bSizer3.Add( self.m_textCtrl15, 0, wx.TOP|wx.BOTTOM|wx.RIGHT|wx.ALIGN_RIGHT, 5 )

		bSizer5 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText18 = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"電話索引:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText18.Wrap( -1 )

		bSizer5.Add( self.m_staticText18, 0, wx.ALL, 5 )

		self.m_textCtrl18 = wx.TextCtrl( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 120,30 ), 0 )
		bSizer5.Add( self.m_textCtrl18, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )


		bSizer3.Add( bSizer5, 1, wx.EXPAND, 5 )

		self.m_staticText12 = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"電話號碼:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )

		bSizer3.Add( self.m_staticText12, 0, wx.ALL, 5 )

		self.m_textCtrl19 = wx.TextCtrl( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 120,30 ), 0 )
		bSizer3.Add( self.m_textCtrl19, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )


		sbSizer1.Add( bSizer3, 1, wx.EXPAND, 5 )

		bSizer4 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText10 = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"操作: 1.新增 2.更改 3.刪除", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText10.Wrap( -1 )

		bSizer4.Add( self.m_staticText10, 0, wx.ALL, 5 )

		self.m_textCtrl20 = wx.TextCtrl( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 120,30 ), 0 )
		bSizer4.Add( self.m_textCtrl20, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )

		self.m_button20 = wx.Button( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Check", wx.DefaultPosition, wx.Size( 120,-1 ), 0 )
		bSizer4.Add( self.m_button20, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )


		sbSizer1.Add( bSizer4, 1, wx.EXPAND, 5 )


		self.SetSizer( sbSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_textCtrl15.Bind( wx.EVT_TEXT_ENTER, self.text4 )
		self.m_textCtrl20.Bind( wx.EVT_TEXT, self.text5 )
		self.m_button20.Bind( wx.EVT_BUTTON, self.create_check )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def text4( self, event ):
		event.Skip()

	def text5( self, event ):
		event.Skip()

	def create_check( self, event ):
		event.Skip()


###########################################################################
## Class CH
###########################################################################

class CH ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"警告!!!", pos = wx.DefaultPosition, size = wx.Size( 291,104 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer7 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText13 = wx.StaticText( self, wx.ID_ANY, u"您確定要刪除?", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText13.Wrap( -1 )

		bSizer7.Add( self.m_staticText13, 0, wx.ALL, 5 )

		self.m_button10 = wx.Button( self, wx.ID_ANY, u"Sure", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer7.Add( self.m_button10, 1, wx.ALL|wx.ALIGN_RIGHT, 5 )


		self.SetSizer( bSizer7 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button10.Bind( wx.EVT_BUTTON, self.check )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def check( self, event ):
		event.Skip()


