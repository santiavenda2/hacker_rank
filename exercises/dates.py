from datetime import date

OUTPUT_FORMAT = "%Y-%m-%d"

MONTH_NAMES = {
    "Jan": 1,
    "Feb": 2,
    "Mar": 3,
    "Apr": 4,
    "May": 5,
    "Jun": 6,
    "Jul": 7,
    "Aug": 8,
    "Sep": 9,
    "Oct": 10,
    "Nov": 11,
    "Dec": 12,
}


def reformate_date(date_string):
    day_s, month_s, year_s = date_string.split(' ')
    year = int(year_s)
    month = int(MONTH_NAMES[month_s])
    day = int(day_s[0:-2])
    d = date(year, month, day)
    return d.strftime(OUTPUT_FORMAT)


if __name__ == '__main__':
    date_s = "6th Oct 2052"
    print reformate_date(date_s)