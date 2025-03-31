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
        self.radio_mouse4 = wx.RadioButton(panel, label="0x05 (Mouse 4)", style = wx.RB_GROUP)
        self.radio_mouse5 = wx.RadioButton(panel, label="0x06 (Mouse 5)")
        self.radio_alt = wx.RadioButton(panel, label="0x12 (Alt)")
        # self.radio_custom = wx.RadioButton(panel, label="Custom:")

        # self.radio_mouse4.Bind(wx.EVT_RADIOBUTTON, self.on_radio_change)
        # self.radio_mouse5.Bind(wx.EVT_RADIOBUTTON, self.on_radio_change)
        # self.radio_alt.Bind(wx.EVT_RADIOBUTTON, self.on_radio_change)
        # self.radio_custom.Bind(wx.EVT_RADIOBUTTON, self.on_radio_change)

        # self.custom_key_label = wx.StaticText(panel, label="Nhấn phím để gán...")
        vbox.Add(self.radio_mouse4, flag=wx.LEFT | wx.TOP, border=10)
        vbox.Add(self.radio_mouse5, flag=wx.LEFT | wx.TOP, border=10)
        vbox.Add(self.radio_alt, flag=wx.LEFT | wx.TOP, border=10)
        # vbox.Add(self.radio_custom, flag=wx.LEFT | wx.TOP, border=10)
        # vbox.Add(self.custom_key_label, flag=wx.LEFT | wx.TOP, border=5)

        # self.key_button = wx.Button(panel, label="Gán phím")
        # self.key_button.Bind(wx.EVT_BUTTON, self.start_key_capture)
        # vbox.Add(self.key_button, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=10)

        self.key_button = wx.Button(panel, label="Start")
        self.key_button.Bind(wx.EVT_BUTTON, self.start_cheating)
        vbox.Add(self.key_button, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=10)

        self.terminal_output = wx.TextCtrl(panel, style=wx.TE_MULTILINE | wx.TE_READONLY | wx.TE_RICH2, size=(-1, 100))
        vbox.Add(self.terminal_output, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)
        
        panel.SetSizer(vbox)

        # self.Bind(wx.EVT_KEY_DOWN, self.on_key_press)

        self.Centre()
        self.Show()

    def log(self, message):
        self.terminal_output.AppendText(message + "\n")

    def start_key_capture(self, event):
        self.custom_key_label.SetLabel("Nhấn phím hoặc chuột...")
        self.SetFocus()

    # def on_key_press(self, event):
    #     key_code = event.GetKeyCode()
    #     if key_code == wx.WXK_ALT:
    #         self.radio_alt.SetValue(True)
    #     else:
    #         self.radio_custom.SetValue(True)
    #         self.custom_key_label.SetLabel(f"Custom: 0x{key_code:02X}")
    #     self.log(f"Phím nhấn: 0x{key_code:02X}")

    # def on_radio_change(self, event):
    #     if self.radio_custom.GetValue():
    #         self.custom_key_label.Show()
    #         self.key_button.Show()
    #     else:
    #         self.custom_key_label.Hide()
    #         self.key_button.Hide()
    #     self.Layout()

    def start_cheating(self, event):
        cheating_main()