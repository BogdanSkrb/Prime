import ctypes

WIDTH, HEIGHT = int(ctypes.windll.user32.GetSystemMetrics(0)/2), int(ctypes.windll.user32.GetSystemMetrics(1)/2)
