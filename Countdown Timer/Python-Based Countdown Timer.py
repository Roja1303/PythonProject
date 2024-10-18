import time
def countdown_time(seconds):
    """countdown functions that takes seconds as input and prints the remaining time every seconds"""
    while seconds:
        #Gets minutes and seconds from total seconds

        mins,secs = divmod(seconds,60)

        #format the time as mm:ss

        time_format = '{:02d}:{:02d}'.format(mins,secs)
        print(time_format)

    #print the time on same line
        time.sleep(1)   #wait for 1 second
        seconds -= 1  #Decrement the total time by 1 second
    print(("Time's up")) #Print message when countdown finishes

if __name__ == '__main__':
    #Input validation
    try:
        #Ask the user to input the countdown time in seconds
        total_seconds = int(input("Enter the time in seconds: "))
        if total_seconds > 0:
            countdown_time(total_seconds)
        else:
            print("Please enter a time greater than zero.")
    except ValueError:
        print("Invalid input! Please enter an integer value.")



