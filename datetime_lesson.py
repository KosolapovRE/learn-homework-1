from datetime import date, timedelta
import locale
locale.setlocale(locale.LC_ALL, 'ru_RU')
from dateutil.relativedelta import relativedelta

dt_today = date.today()
print(dt_today)
delta = timedelta(days = 1)
dt_yesterday = dt_today - delta
print(dt_yesterday)
dt_month_later = dt_today - relativedelta(months=1)
print(dt_month_later)

from datetime import datetime
dt_str = "01/01/17 12:10:03.234567"
dt_new = datetime.strptime(dt_str, '%m/%d/%y %H:%M:%S.%f')
print(dt_new)
print(dt_new.strftime('%A %d %B %Y'))
