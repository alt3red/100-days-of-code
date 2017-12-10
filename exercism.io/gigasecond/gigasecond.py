from datetime import datetime
import calendar

def add_gigasecond(birth_date):
    bd = calendar.timegm(birth_date.timetuple()) + 1000000000
    return datetime.utcfromtimestamp(bd)
    
