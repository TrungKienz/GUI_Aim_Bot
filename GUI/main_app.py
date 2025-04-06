import threading
import wx

from CORE.cheating_main import cheating_main

class MainAppFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, title="Main App", size=(400, 600), style=wx.DEFAULT_FRAME_STYLE & ~(wx.RESIZE_BORDER | wx.MAXIMIZE_BOX))
        panel = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)

        sensitivity_label = wx.StaticText(panel, label="Độ nhạy:")
        self.sensitivity_input = wx.TextCtrl(panel, value="0.2")
        vbox.Add(sensitivity_label, flag=wx.LEFT | wx.TOP, border=10)
        vbox.Add(self.sensitivity_input, flag=wx.EXPAND | wx.LEFT | wx.RIGHT, border=10)

        pov_label = wx.StaticText(panel, label="Điều chỉnh khoảng nhận diện:")
        self.fov_input = wx.TextCtrl(panel, value="100")
        vbox.Add(pov_label, flag=wx.LEFT | wx.TOP, border=10)
        vbox.Add(self.fov_input, flag=wx.EXPAND | wx.LEFT | wx.RIGHT, border=10)

        active_program_label = wx.StaticText(panel, label="Tùy chọn gán phím để bật chương trình:")
        vbox.Add(active_program_label, flag=wx.LEFT | wx.TOP, border=10)
        self.radio_mouse4 = wx.RadioButton(panel, label="Chuột phụ 1", style = wx.RB_GROUP)
        self.radio_mouse5 = wx.RadioButton(panel, label="Chuột phụ 2")
        self.radio_alt = wx.RadioButton(panel, label="Alt")

        vbox.Add(self.radio_mouse4, flag=wx.LEFT | wx.TOP, border=10)
        vbox.Add(self.radio_mouse5, flag=wx.LEFT | wx.TOP, border=10)
        vbox.Add(self.radio_alt, flag=wx.LEFT | wx.TOP, border=10)

        resolution_label = wx.StaticText(panel, label="Chọn độ phân giải của màn hình:")
        vbox.Add(resolution_label, flag=wx.LEFT | wx.TOP, border=10)
        self.radio_fhd = wx.RadioButton(panel, label="Màn hình Full HD (1920x1080)", style = wx.RB_GROUP)
        self.radio_2k = wx.RadioButton(panel, label="Màn hình 2K (2560x1440)")
        self.radio_4k = wx.RadioButton(panel, label="Màn hình 4K (3840x2160)")

        vbox.Add(self.radio_fhd, flag=wx.LEFT | wx.TOP, border=10)
        vbox.Add(self.radio_2k, flag=wx.LEFT | wx.TOP, border=10)
        vbox.Add(self.radio_4k, flag=wx.LEFT | wx.TOP, border=10)

        character_outline_label = wx.StaticText(panel, label="Chọn đường viền nhân vật:")
        vbox.Add(character_outline_label, flag=wx.LEFT | wx.TOP, border=10)
        self.radio_purple = wx.RadioButton(panel, label="Đường viền tím", style = wx.RB_GROUP)
        self.radio_red = wx.RadioButton(panel, label="Đường viền đỏ")
        self.radio_yellow = wx.RadioButton(panel, label="Đường viền vàng")

        vbox.Add(self.radio_purple, flag=wx.LEFT | wx.TOP, border=10)
        vbox.Add(self.radio_red, flag=wx.LEFT | wx.TOP, border=10)
        vbox.Add(self.radio_yellow, flag=wx.LEFT | wx.TOP, border=10)


        self.key_button = wx.Button(panel, label="Start")
        self.key_button.Bind(wx.EVT_BUTTON, self.start_cheating)
        vbox.Add(self.key_button, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=10)

        self.terminal_output = wx.TextCtrl(panel, style=wx.TE_MULTILINE | wx.TE_READONLY | wx.TE_RICH2, size=(-1, 100))
        vbox.Add(self.terminal_output, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)
        
        panel.SetSizer(vbox)


        self.Centre()
        self.Show()

    def log(self, message):
        # self.terminal_output.AppendText(message + "\n")
        wx.CallAfter(self.terminal_output.AppendText, message + "\n")

    def start_cheating(self, event):
        if self.radio_mouse4.GetValue():
            hold_key = '0x05'
        elif self.radio_mouse5.GetValue():
            hold_key = '0x06'
        elif self.radio_alt.GetValue():
            hold_key = '0xA4'
        
        if self.radio_fhd.GetValue():
            center_x, center_y = 1920 // 2, 1080 // 2
        elif self.radio_2k.GetValue():
            center_x, center_y = 2560 // 2, 1440 // 2
        elif self.radio_4k.GetValue():
            center_x, center_y = 3840 // 2, 2160 // 2

        if self.radio_purple.GetValue():
            border_color = 'purple'
        elif self.radio_red.GetValue():
            border_color = 'red'
        elif self.radio_yellow.GetValue(): 
            border_color = 'yellow'

        try:
            fov = int(self.fov_input.GetValue())
            sensitivity = float(self.sensitivity_input.GetValue())
            self.log("Độ nhạy chuột: " + str(sensitivity))
        except ValueError:
            self.log("Giá trị độ nhạy không hợp lệ.")
            return

        def run_cheating():
            try:
                cheating_main(fov=fov,center_x=center_x, center_y=center_y, mouse_sensitivity=sensitivity, border_color=border_color, hold_key=hold_key, log_func=self.log)
                wx.CallAfter(self.log, "Chương trình đã bắt đầu.") 
            except Exception as e:
                wx.CallAfter(self.log, f"Lỗi: {e}")

        threading.Thread(target=run_cheating, daemon=True).start()