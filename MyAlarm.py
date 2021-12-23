import datetime
import winsound


def alarm(time):
    # This function will take a string as a time and return in the format that you will specify in the second argument

    # %I means the clock will be of 12 hour hours <= ex- after 12 there is 1 PM,2 PM,3 PM or before 12 PM,11 AM,5 AM  (by default it is 24 hours <= ex-23,21,19 )
    # %M means minutes in the form of decimals like 1 minute 59 minutes etc
    # %p will specify the time in AM OR PM format
    formatted_time = str(datetime.datetime.now().strptime(time, "%I:%M %p"))
    # print(formatted_time)  # 1900-01-01 02:40:00
    # Now we have to separate hour and minute from the formatted_time variable

    # slicing the hour out from the formatted_time variable and converting it into an integer
    hour = formatted_time[11:-6]
    hour = int(hour)

    # slicing the minute out from the formatted_time variable and converting it into an integer
    # This will slice out the element in the 14th index to 16-1 (-1 because it gives the previous element of the given element that is 15)
    minute = formatted_time[14:16]
    minute = int(minute)

    print(f"Sir your Alarm is successfully set for {time}")

    while(True):
        if datetime.datetime.now().hour == hour:
            if datetime.datetime.now().minute == minute:
                print("wake up sir!")
                winsound.PlaySound(
                    'mp3_files/Freshstart.wav', winsound.SND_LOOP)

            elif datetime.datetime.now().minute > minute:
                print("Alarm Stopped !")
                break
