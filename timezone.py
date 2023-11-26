import time
import pytz
from datetime import datetime

local_time_str = time.strftime('%Y-%m-%d %H:%M:%S')
local_datetime = datetime.strptime(local_time_str, '%Y-%m-%d %H:%M:%S')

# Iterate through a list of common timezones and check if the local time is in that timezone
timezones_to_check = ['America/New_York', 'America/Chicago', 'America/Los_Angeles', 'UTC']

local_timezone = None

for tz_name in timezones_to_check:
    tz = pytz.timezone(tz_name)
    if tz.utcoffset(local_datetime) == local_datetime.utcoffset():
        local_timezone = tz
        break

if local_timezone:
    print("Local time is in timezone:", local_timezone)
    
    # Convert the local time to Eastern Standard Time (EST)
    est_tz = pytz.timezone('America/New_York')
    est_time = local_timezone.localize(local_datetime).astimezone(est_tz)
    
    print("Local Time:", local_datetime.strftime('%Y-%m-%d %H:%M:%S %Z'))
    print("EST Time:", est_time.strftime('%Y-%m-%d %H:%M:%S %Z'))
    print("EST Timezone:", est_tz)
else:
    print("Unable to determine the local timezone.")
