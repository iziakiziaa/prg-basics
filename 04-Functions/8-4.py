#  Define a function time_string(hours, minutes, time_format) that, given the number of hours (0..23) and the number of minutes (0..59), 
#  returns a string specifying the time in the given format ('24' for 24-hour time and '12' for 12-hour time).

#  Then write a program that tests whether the function works correctly.

def time_string(hours, minutes, time_format):
    if time_format == '24':
        return f"{hours:02d}:{minutes:02d}"
    elif time_format == '12':
        am_pm = 'am' if hours < 12 else 'pm'
        if hours == 0:
            display_hour = 12
        elif hours > 12:
            display_hour = hours - 12
        else:
            display_hour = hours
        return f'{display_hour}:{minutes:02d}{am_pm}'
    else:
        return "Invalid time format specified. Use '24' or '12'."
    
print(f'time_string(15,38,"24") returns {time_string(15, 38, '24')}')
print(f'time_string(11,15,"12") returns {time_string(11, 15, '12')}')
print(f'time_string(13, 10,"12") returns {time_string(13, 10, '12')}')