import time
from src.os_utils.sensor import get_active_window_info
from src.storage.db import initialize_db, save_session
from src.core.config import load_config 

def run_tracker():
    print("Tracker starting up...")
    
    try:
        initialize_db()
    except Exception as e:
        print(f"CRITICAL ERROR: Could not initialize database. {e}")
        return
        
    config = load_config()
    whitelist = config.get("games", [])
    print(f"Loaded whitelist with {len(whitelist)} games.")
        
    print("Tracker active. Press Ctrl+C to stop.")
    
    current_exe = None
    start_time = None
    
    try:
        while True:
            _, _, _, exe_name = get_active_window_info()
            
            if exe_name != current_exe:
                if current_exe is not None:
                    end_time = time.time()
                    elapsed_time = end_time - start_time
                    print(f"Finished playing [{current_exe}]. Session length: {elapsed_time:.1f} seconds.")
                    try:
                        save_session(current_exe, start_time, end_time)
                    except Exception as e:
                        print(f"ERROR: Failed to save session to database. {e}")
                    
                    current_exe = None
                    start_time = None
                
                if exe_name in whitelist:
                    current_exe = exe_name
                    start_time = time.time()
                    print(f"Started playing [{current_exe}]...")
            
            time.sleep(2)
            
    except KeyboardInterrupt:
        if current_exe is not None:
            print(f"\nShutting down. Saving final session for [{current_exe}]...")
            try:
                save_session(current_exe, start_time, time.time())
            except Exception as e:
                print(f"ERROR: Failed to save final session. {e}")
                
        print("Tracker gracefully shut down.")

if __name__ == "__main__":
    run_tracker()