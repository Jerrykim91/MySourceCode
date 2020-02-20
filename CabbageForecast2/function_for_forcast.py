#  입력값을 월 , 일  시간을  문자열로 변경 
# # date = datetime(2015, 12, 31, 14, 0, 0)

def make_fdate(date):
    # 10이상인 것들은 문자열로 변경 
    year = str(date.year)
    if date.month >= 10:
        month = str(date.month)
        # 1자리수는 문자열 만든후 문자열 0을 붙임
    else:
        month = "0"+str(date.month)
    if date.day >= 10:
        day = str(date.day)
    else:
        day = "0"+str(date.day)
    hour = str(date.hour)

    fdate = year + "." + month + "." + day + "." + hour + ":00"
    return fdate