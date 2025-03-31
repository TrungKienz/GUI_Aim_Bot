# AIM BOT PROJECT 

# BUILD APP 
Đóng gói ứng dụng thành file .exe:
pyinstaller --onefile --windowed app.py

--onefile: Tạo một file .exe duy nhất.
--windowed: Ẩn terminal khi chạy (chỉ dùng cho ứng dụng có GUI).

Tùy chỉnh icon và tên file:
pyinstaller --onefile --windowed --name MyApp --icon=myicon.ico app.py

--name MyApp: Đặt tên file .exe là MyApp.exe.

--icon=myicon.ico: Đặt icon cho ứng dụng.