import ctypes

MB_OK = 0x0
MB_ICONERROR = 0x10
MB_TOPMOST = 0x40000

def showerror(title: str, message: str):
  ctypes.windll.user32.MessageBoxW(0, message, title, MB_OK | MB_ICONERROR | MB_TOPMOST)
