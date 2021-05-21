import winsound
#general frequency 2500
frequency = int(input("enter the frequency:"))
duration = int(input("enter the duration 1000ms is 1 sec:"))
winsound.Beep(frequency,duration)