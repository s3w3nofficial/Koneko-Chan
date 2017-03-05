def main(time):
    #time = '10:02:AM'
    time_array = time.split(":")
    alarm_time = 0
    if time_array[2] == 'PM':
        a = time_array[0]
        b = 12 + int(a)
        time_array[0] = str(b)
    time_array.pop(2)
    alarm_time += int(time_array[0]) * 3600
    alarm_time += int(time_array[1]) * 60
    
    print time_array, alarm_time

if __name__ == "__main__":
    main("10:02:PM")