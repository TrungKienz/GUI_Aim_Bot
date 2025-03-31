import wx

class LoginFrame(wx.Frame):
    def __init__(self, on_login_success):
        super().__init__(parent=None, title="Kích hoạt Valorant ANT BOT", size=(350, 200),
                         style=wx.DEFAULT_FRAME_STYLE & ~(wx.RESIZE_BORDER | wx.MAXIMIZE_BOX))
        
        self.on_login_success = on_login_success  
        panel = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)

        self.title = wx.StaticText(panel, label="Kích Hoạt", style=wx.ALIGN_CENTER)
        font = wx.Font(14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)
        self.title.SetFont(font)
        vbox.Add(self.title, flag=wx.ALIGN_CENTER | wx.TOP, border=20)

        self.user_label = wx.StaticText(panel, label="Mã kích hoạt phần mềm:")
        vbox.Add(self.user_label, flag=wx.LEFT | wx.TOP, border=10)
        self.activate_key_text = wx.TextCtrl(panel)
        vbox.Add(self.activate_key_text, flag=wx.EXPAND | wx.LEFT | wx.RIGHT, border=10)

        self.login_button = wx.Button(panel, label="Kích hoạt")
        self.login_button.Bind(wx.EVT_BUTTON, self.on_login)
        vbox.Add(self.login_button, flag=wx.ALIGN_CENTER | wx.TOP, border=20)

        panel.SetSizer(vbox)
        self.Centre()
        self.Show()

    def on_login(self, event):
        activate_key = self.activate_key_text.GetValue()

        if activate_key == "1234":  
            wx.MessageBox("Kích hoạt thành công!", "Info", wx.OK | wx.ICON_INFORMATION)
            self.Destroy()  
            self.on_login_success()  
        else:
            wx.MessageBox("Mã kích hoạt không khả dụng hoặc đã hết hạn. \nVui lòng liên hệ quản trị viên để được nhận mã!", "Error", wx.OK | wx.ICON_ERROR)
