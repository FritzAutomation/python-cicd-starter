import schedule
import time

def hello_world():
    print("Hello, world!")

if __name__ == "__main__":
    # Schedule the hello_world function to run every 10 seconds
    schedule.every(10).seconds.do(hello_world)

    # Keep the script running to execute the scheduled tasks
    while True:
        schedule.run_pending()
        time.sleep(1)  # Sleep for 1 second before checking the schedule again
