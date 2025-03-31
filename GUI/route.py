import wx
from .login import LoginFrame
from .main_app import MainAppFrame

class AppRouter(wx.App):
    def OnInit(self):
        self.login_frame = LoginFrame(on_login_success=self.open_main_app)
        return True

    def open_main_app(self):
        self.main_app_frame = MainAppFrame()
        self.main_app_frame.Show()

def router():
    app = AppRouter(False)
    app.MainLoop()
