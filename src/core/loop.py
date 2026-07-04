import time
from src.storage.db import initialize_db,save_session
from src.os_utils.sensor import get_active_window_info


def run_tracker():
    print("Tracker starting...")

    try:
        initialize_db()
    except Exception as e:
        print(f"An error occurred: {e}")
        return
    
    print("Tracker active. Press Ctrl+C to stop.")

    curr_exe = None
    start_time = None

    try:
        while True:
            _, _, _, exe_name = get_active_window_info()

            if exe_name != curr_exe:
                if curr_exe is not None:
                    end_time = time.time()
                    elapsed_time = end_time - start_time

                    print(f"Finished playing [{curr_exe}] for {elapsed_time:.2f} seconds.")

                    try:
                        save_session(curr_exe, start_time, end_time)
                    except Exception as e:
                        print(f"An error occurred while saving session: {e}")
                
                curr_exe = exe_name
                start_time = time.time()
                print(f"Started playing [{curr_exe}]...")

            time.sleep(2)

    except KeyboardInterrupt:
        if curr_exe is not None:
            print("Stopping tracker. Saving final session for [{curr_exe}]...")
            try:
                save_session(curr_exe, start_time, time.time())
            except Exception as e:
                print(f"An error occurred while saving final session: {e}")
        
        print("Tracker stopped. Goodbye!")
    
if __name__ == "__main__":
    run_tracker()
