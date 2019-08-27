
import wx
import NotePad_GUI   #wxpythonbuilding產生GUI.py
import os

class mycall(NotePad_GUI.MyFrame1):
    
    def BD(self, event):
        self.Close()
        w = wx.App()
        p = mycall(None)
        p.Show()
        w.MainLoop()
        
        # self.m_richText2.Clear()
        # self.SetTitle("檔案名稱")
        
    def OP(self, event):
        FileName = wx.FileSelector(
            "開啟舊檔",
            wildcard = "文件檔 (*.txt)|*.txt",
            flags = wx.FD_OPEN
        )
        if FileName:
            rf = os.path.basename(FileName)
            self.SetTitle(rf)
            with open(FileName,"r") as f:
                self.m_richText2.SetValue(f.read()) # Read()讀取內部檔案內容。

    def SV( self, event):
        tt = self.GetTitle()
        #兩種方法寫存檔檔案。
        # f = open(FileName,"w")
        # f.write(ctt)
        # f.close()
        ctt = self.m_richText2.GetValue()   #尋找筆記本內容也就是值。
        if tt !="檔案名稱":
            f = open(tt,"w")
            f.write(ctt)
            f.close()
        else:
            FileName = wx.FileSelector(
            "儲存檔案",
            wildcard = "TEXT (*.txt)|*.txt",
            flags = wx.FD_SAVE          
            )
            if FileName:
                rf = os.path.basename(FileName)
                self.SetTitle(rf) 
                f = open(FileName,"w")
                f.write(ctt)
                f.close()

    def CL(self , event):
        self.Close()
           
w = wx.App()
p = mycall(None)
p.Show()
w.MainLoop()

