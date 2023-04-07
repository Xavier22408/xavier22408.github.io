# from datetime import datetime, timedelta
# import json
# from ics import Calendar, Event
# import pytz


# def convert_time_to_24_hour_format(time_str):
#     dt_obj = datetime.strptime(time_str, "%I:%M %p")
#     return dt_obj.strftime("%H:%M")


# def generate_ics(group_name):
#     with open('data.json', 'r', encoding='utf-8') as f:
#         data = json.load(f)

#     c = Calendar()

#     for item in data:
#         if item['group_name'] == group_name:
#             event = Event()
#             event.name = item['Subject_short']
#             event.organizer = item['educators']
#             event.description = item['educators'] + '\n' + item['Subject']
#             start_time = datetime.strptime(item['date'] + ' ' + item['time_start'], "%Y-%m-%d %I:%M %p")
#             end_time = datetime.strptime(item['date'] + ' ' + item['time_end'], "%Y-%m-%d %I:%M %p")

#             # check if end_time or start_time is <10, increase by 12 hours
#             if start_time.hour < 10:
#                 start_time = start_time + timedelta(hours=12)
#             if end_time.hour < 10:
#                 end_time = end_time + timedelta(hours=12)

#             event.begin = start_time.astimezone(pytz.timezone('Europe/Moscow'))
#             event.end = end_time.astimezone(pytz.timezone('Europe/Moscow'))
#             c.events.add(event)

#     with open('schedule.ics', 'w', encoding='utf-8') as my_file:
#         my_file.writelines(c)
from datetime import datetime, timedelta
import json
from ics import Calendar, Event
import pytz


def convert_time_to_24_hour_format(time_str):
    dt_obj = datetime.strptime(time_str, "%I:%M %p")
    return dt_obj.strftime("%H:%M")


def generate_ics(group_name):
    with open('data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    c = Calendar()

    for item in data:
        if item['group_name'] == group_name:
            event = Event()
            event.name = item['Subject_short']
            event.organizer = item['educators']
            event.description = item['educators'] + '\n' + item['Subject']
            start_time_str = item['date'] + ' ' + item['time_start']
            end_time_str = item['date'] + ' ' + item['time_end']

            start_time = datetime.strptime(start_time_str, "%Y-%m-%d %I:%M %p")
            end_time = datetime.strptime(end_time_str, "%Y-%m-%d %I:%M %p")

            # check if start time is before 10am, convert to PM time
            if start_time.hour < 10:
                start_time = start_time + 12
                end_time = end_time + 12

            event.begin = start_time.astimezone(pytz.timezone('Europe/Moscow'))
            event.end = end_time.astimezone(pytz.timezone('Europe/Moscow'))
            c.events.add(event)

    with open('schedule.ics', 'w', encoding='utf-8') as my_file:
        my_file.writelines(c)
