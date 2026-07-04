import time 
from src.os_utils.sensor import get_active_window_info

def run_tracker():
    print("Tracker started. Press Ctrl+C to stop.")

    curr_exe = None
    start_time = None

    try:
        while True:
            _, _, _, exe_name = get_active_window_info()

            if exe_name != curr_exe:
                if curr_exe is not None:
                    elapsed_time = time.time() - start_time
                    print(f"Application: {curr_exe}, Time Spent: {elapsed_time:.2f} seconds")

                curr_exe = exe_name
                start_time = time.time()
                print(f"Switched to application: {curr_exe}...")

            time.sleep(2)

    except KeyboardInterrupt:
        if curr_exe is not None:
            elapsed_time = time.time() - start_time
            print(f"Application: {curr_exe}, Time Spent: {elapsed_time:.2f} seconds")
        print("Tracker stopped.")

if __name__ == "__main__":
    run_tracker()
