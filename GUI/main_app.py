import wx

from CORE.cheating_main import cheating_main

class MainAppFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, title="Main App", size=(400, 450))
        panel = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)

        sensitivity_label = wx.StaticText(panel, label="Độ nhạy:")
        self.sensitivity_input = wx.TextCtrl(panel)
        vbox.Add(sensitivity_label, flag=wx.LEFT | wx.TOP, border=10)
        vbox.Add(self.sensitivity_input, flag=wx.EXPAND | wx.LEFT | wx.RIGHT, border=10)

        active_program_label = wx.StaticText(panel, label="Tùy chọn gán phím để bật chương trình:")
        vbox.Add(active_program_label, flag=wx.LEFT | wx.TOP, border=10)
        self.radio_mouse4 = wx.RadioButton(panel, label="Chuột phụ 1", style = wx.RB_GROUP)
        self.radio_mouse5 = wx.RadioButton(panel, label="Chuột phụ 2")
        self.radio_alt = wx.RadioButton(panel, label="Alt")

        vbox.Add(self.radio_mouse4, flag=wx.LEFT | wx.TOP, border=10)
        vbox.Add(self.radio_mouse5, flag=wx.LEFT | wx.TOP, border=10)
        vbox.Add(self.radio_alt, flag=wx.LEFT | wx.TOP, border=10)


        self.key_button = wx.Button(panel, label="Start")
        self.key_button.Bind(wx.EVT_BUTTON, self.start_cheating)
        vbox.Add(self.key_button, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=10)

        self.terminal_output = wx.TextCtrl(panel, style=wx.TE_MULTILINE | wx.TE_READONLY | wx.TE_RICH2, size=(-1, 100))
        vbox.Add(self.terminal_output, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)
        
        panel.SetSizer(vbox)


        self.Centre()
        self.Show()

    def log(self, message):
        self.terminal_output.AppendText(message + "\n")

    def start_cheating(self, event):
        if self.radio_mouse4.GetValue():
            hold_key = '0x05'
            self.log(self.sensitivity_input.GetValue())
        elif self.radio_mouse5.GetValue():
            hold_key = '0x06'
        elif self.radio_alt.GetValue():
            hold_key = '0xA4'

        
        
        cheating_main(hold_key=hold_key)