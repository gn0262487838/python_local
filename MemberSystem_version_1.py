import wx
import MemberSystem_version_1_GUI
import pymysql
import prettytable as pt
import os

# Start #

# 連接資料庫
MemberSystem = pymysql.connect(
host = "localhost",
user = "root",
passwd = "",
db = "membersystem",
charset = "utf8"
)
# 獲得操作游標
cmd = MemberSystem.cursor()

# 全域變數
w = ""
v = ""

# 主視窗_會員基本資料
class MSM(MemberSystem_version_1_GUI.MyFrame1):
    
    # 新增會員資料
    def create_add(self, event):
        a = self.m_textCtrl5.GetValue()
        b = self.m_textCtrl6.GetValue()
        c = self.m_textCtrl7.GetValue()
        d = self.m_textCtrl8.GetValue()
        if d != "":
            return self.m_statusBar1.SetStatusText("不需要輸入編號!!!")
        if str.isalpha(a):
            if len(b) == 8 and str.isdigit(b):
                if str.isalnum(c) or c == "":
                    cmd.execute(
                    "insert into `member`(`name`,`borned_date`,`address`) values(%s,%s,%s)"
                    ,(a,b,c)
                    )
                    MemberSystem.commit()
                    self.m_textCtrl5.Clear()
                    self.m_textCtrl6.Clear()
                    self.m_textCtrl7.Clear()
                    self.m_statusBar1.SetStatusText("")
                else:
                    return self.m_statusBar1.SetStatusText("TypeError:無法辨識地址資料,ex.可能有非字母的符號!")
            else:
                return self.m_statusBar1.SetStatusText("TypeError:非西元格式,ex.19XX12XX")
        else:
            return self.m_statusBar1.SetStatusText("TypeError:姓名須為中文或英文")
        self.create_show(event)
    
    # 更改會員資料
    def create_change(self,event):
        a = self.m_textCtrl5.GetValue()
        b = self.m_textCtrl6.GetValue()
        c = self.m_textCtrl7.GetValue()
        d = self.m_textCtrl8.GetValue()
        if str.isdigit(d):
            if str.isalpha(a) and a !="":
                cmd.execute(
                "update `member` set `name`=%s where id`=%s"
                ,(a, d) 
                )
                MemberSystem.commit() 
                if len(b) == 8 and str.isdigit(b):
                    cmd.execute(
                    "update `member` set `borned_date`=%s where `id`=%s"
                    ,(b, d) 
                    )
                    MemberSystem.commit()
                elif b == "":
                    if str.isalnum(c):
                        cmd.execute(
                        "update `member` set `address`=%s where `id`=%s"
                        ,(c, d ) 
                        )
                        MemberSystem.commit()  
                    elif c =="":
                        return self.m_statusBar1.SetStatusText("==========無資料異動==========")
                    else:
                        return self.m_statusBar1.SetStatusText("TypeError:無法辨識地址資料")
                return self.m_statusBar1.SetStatusText("TypeError:非西元格式,ex.19XX12XX or 非編號格式")
            elif a == "":
                if len(b) == 8 and str.isdigit(b):
                    cmd.execute(
                    "update `member` set `borned_date`=%s where `id`=%s"
                    ,(b, d) 
                    )
                    MemberSystem.commit()
                elif b == "":
                    if str.isalnum(c):
                        cmd.execute(
                        "update `member` set `address`=%s where `id`=%s"
                        ,(c, d ) 
                        )
                        MemberSystem.commit()
                    elif c =="":
                        return self.m_statusBar1.SetStatusText("==========無資料異動==========")
                    else:
                        return self.m_statusBar1.SetStatusText("TypeError:無法辨識地址資料")
                else:  
                    return self.m_statusBar1.SetStatusText("TypeError:非西元格式,ex.19XX12XX or 非編號格式")
            else:
                return self.m_statusBar1.SetStatusText("TypeError:姓名須為中文或英文")    
        else:
            return self.m_statusBar1.SetStatusText("TypeError:非編號格式 ex. 1 or 12...")
        self.m_textCtrl5.Clear()
        self.m_textCtrl6.Clear()
        self.m_textCtrl7.Clear()
        self.m_textCtrl8.Clear()
        self.m_statusBar1.SetStatusText("")
        self.create_show(event)

    # 刪除會員資料
    def create_delete(self,event):
        a = self.m_textCtrl5.GetValue()
        b = self.m_textCtrl6.GetValue()
        c = self.m_textCtrl7.GetValue()
        d = self.m_textCtrl8.GetValue()
        if a != "":
            return self.m_statusBar1.SetStatusText("姓名、生日、住址不需輸入")
        elif b != "":
            return self.m_statusBar1.SetStatusText("姓名、生日、住址不需輸入")
        elif c != "":
            return self.m_statusBar1.SetStatusText("姓名、生日、住址不需輸入")
        
        if str.isdigit(d):
            cmd.execute(
            "delete from `member` where `id` = %s"
            , (d)
            )
            MemberSystem.commit()
        else:
            return self.m_statusBar1.SetStatusText("TypeError:非編號格式")
        self.m_textCtrl5.Clear()
        self.m_textCtrl6.Clear()
        self.m_textCtrl7.Clear()
        self.m_textCtrl8.Clear()
        self.m_statusBar1.SetStatusText("")
        self.create_show(event)

    # 顯示目前會員資料
    def create_show(self, event):
        v = self.m_textCtrl30
        v.Clear()
        self.m_textCtrl5.Clear()
        self.m_textCtrl6.Clear()
        self.m_textCtrl7.Clear()
        self.m_textCtrl8.Clear()
        tb = pt.PrettyTable(["會員編號","姓名","出生年月日","地址","電話索引","會員 編號","電話"])
        

        cmd.execute(
            "select * from `member` left join `tel` on `member`.`id`=`tel`.`member_id` order by `member`.`id` asc "
        )
        lis = cmd.fetchall()
        print(lis)
        for i in lis:
            tb.add_row(i)
        tb.set_style(pt.PLAIN_COLUMNS)
        tb.align = "l"
        TB = str(tb)
        v.SetValue(TB)

    # 離開程式       
    def create_close(self,event):
        MemberSystem.close()
        self.Close()    

    # 打開電話系統
    def create_tel(self, event):
        self.create_show(event)
        exee = CH(self)
        exee.Show() 

# 次視窗_會員電話
class MEM_TEL(MemberSystem_version_1_GUI.TelSystem):

    # 資料確認並送出
    def create_check(self, event):
        global w
        a1 = self.m_textCtrl15.GetValue() 
        b1 = self.m_textCtrl18.GetValue()
        b2 = self.m_textCtrl19.GetValue()
        c1 = self.m_textCtrl20.GetValue()
        if c1 == "1":
            if b1 !="":
                return self.SetTitle("電話系統:電話索引無須輸入!!!")
            cmd.execute(
                "insert into `tel`(`member_id`,`member_tel`) values(%s,%s)"
                ,(a1,b2)
                )
            MemberSystem.commit()
            self.Close()
        elif c1 == "2":
            if a1 !="":
                return self.SetTitle("電話系統:會員編號無須輸入!!!")
            cmd.execute(
            "update `tel` set `member_tel`=%s where `id`=%s"
            ,( b2, b1) 
            )
            MemberSystem.commit()
            self.SetTitle("電話系統")
            self.Close()
        elif c1 == "3":
            CH(None).Show()
            if a1 !="":
                return self.SetTitle("電話系統:會員編號無須輸入!!!")
            if b2 !="":
                return self.SetTitle("電話系統:電話號碼無須輸入!!!")
            
            w == CH.check(self,event):
            if 
                if w == True:
                    cmd.execute(
                        "delete from `tel` where `id`=%s"
                        , (b1) 
                    )
                    MemberSystem.commit()
                    self.SetTitle("電話系統")
                    MSM.create_show(self,event)
                    self.Close()
                else:
                    return self.SetTitle("不刪除!!!")
        else:
            return self.SetTitle("電話系統:操作指令為無效數值")

# 次視窗_警告
class CH(MemberSystem_version_1_GUI.CH):

    # 再次確認
    def check(self,event):
        return True

# 建立視窗並顯示視窗。
windows = wx.App()
exe = MSM(None)  
exe.Show()
windows.MainLoop()

# over #

# 筆記 #
# 不可寫成 exe = MemberSystem_version_1_GUI.MyFrame1(None),因為開啟的視窗是最原始的，只有原始功能!!!

# exee = MEM_TEL(self)
# exee.Show() ，不需要再加上wx.App() & wx.Mainloop()。 一個主視窗已有設定了!

# 表格要呈現在畫面上對齊要去wxbuild裡font>family>Teletype!!!
