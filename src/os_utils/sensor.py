import psutil
import win32gui
import win32process


def get_active_window_info():
    """
    queries the windows os for the currently active window and returns its window handle (hwnd), title, pid and executable name.
    """

    hwnd = win32gui.GetForegroundWindow()
    title = win32gui.GetWindowText(hwnd)

    _, pid = win32process.GetWindowThreadProcessId(hwnd)

    exe_name = "Unknown"

    if pid>0:
        try:
            process = psutil.Process(pid)
            exe_name = process.name()
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    return hwnd, title, pid, exe_name

if __name__ == "__main__":
    hwnd, title, pid, exe_name = get_active_window_info()
    print(f"Active Window Handle: {hwnd}, Title: {title}, PID: {pid}, Executable: {exe_name}")
