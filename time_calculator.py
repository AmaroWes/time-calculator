def add_time(start, duration, *day):

    start = start.split(" ")
    duration = duration.split(" ")

    hours, minutes = (start[0].split(":"))
    d_hours, d_minutes = (duration[0].split(":"))

    week = [
      ["sunday", 0], 
      ["monday", 1], 
      ["tuesday", 2], 
      ["wednesday", 3], 
      ["thursday", 4], 
      ["friday", 5], 
      ["saturday", 6]
    ]

    # transformation to int and variables
    new_hour = int(hours) + int(d_hours)
    new_minute = int(minutes) + int(d_minutes)
    new_day, cont, aux_day = 0, 0, 0

    # time calculation
    if new_minute > 60:
        aux = new_minute // 60
        new_minute %= 60
        new_hour += aux
    
    if new_hour > 12:
        aux = new_hour % 12
        while new_hour >= 12:
            new_hour -= 12
            cont += 1

        previus = start[1]

        if cont % 2 == 0:
            start[1] = start[1]
        else:
            if start[1] == "AM":
                start[1] = "PM"
            else:
                start[1] = "AM"

        if previus != start[1] and previus == "PM": cont += 1

        aux_day += int(cont / 2)
        new_hour = aux

    if new_hour == 12:
        previus = start[1]
        if start[1] == "AM":
            start[1] = "PM"
        else:
            start[1] = "AM"

        if previus != start[1] and previus == "PM": 
            cont += 1
            aux_day += cont



    # transformation to str
    if new_hour == 0:
        new_hour = 12
    new_hour = str(new_hour)

    if new_minute < 10:
        new_minute = "0" + str(new_minute)
    else:
        new_minute = str(new_minute)

    new_time = f"{new_hour}:{new_minute} {start[1]}"
    
    # day verification
    if day:
        day = day[0].lower()
        for i in range(len(week)):
            if day == week[i][0]:
                new_day = week[i][1]
        new_day += aux_day
        if new_day > 0:
            if new_day >= 7:
                new_day %= 7
        
        day = week[new_day][0]
        day = day.replace(day[0], day[0].upper())
        new_time += f", {day}"

    if cont > 0:
        aux = ""
        if int(cont / 2) == 1:
            aux = f"(next day)"
            new_time += f" {aux}"
        elif int(cont / 2) == 0:
            pass
        else:
            aux = f"({int(cont / 2)} days later)"
            new_time += f" {aux}"

    return new_time
