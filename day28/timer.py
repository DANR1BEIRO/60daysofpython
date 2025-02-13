import time

def timer(seconds):
    
    print("Starting timer...")
    
    for sec in range(seconds + 1):
        print(f"Time: {sec} {'second' if sec <= 1 else 'seconds'}", end="\r")
        time.sleep(1) 

    print("\nTIME'S UP!")

if __name__=="__main__":
    timer(5)