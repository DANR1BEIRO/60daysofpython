import time

def ten_sec_countdown():
    timer = 10
    while timer > 0:
        print(f"Countdown:{timer:2}", end="\r")
        time.sleep(1)
        timer -= 1
    print("\nTIME'S UP!")

if __name__=="__main__":
    ten_sec_countdown()