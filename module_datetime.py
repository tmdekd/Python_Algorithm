# -*- coding: utf-8 -*-  # 인코딩 설정

import datetime  # datetime 모듈을 불러옵니다.
import pytz  # pytz 모듈을 불러옵니다.

# 1. 현재 날짜와 시간 가져오기 (datetime.now())
current_datetime = datetime.datetime.now()
print(f"1. 현재 날짜와 시간: {current_datetime}")

# 2. 특정 날짜와 시간 설정하기 (datetime(year, month, day, hour, minute, second))
custom_datetime = datetime.datetime(2023, 5, 17, 15, 30, 45)
print(f"2. 특정 날짜와 시간: {custom_datetime}")

# 3. 현재 날짜만 가져오기 (date.today())
current_date = datetime.date.today()
print(f"3. 현재 날짜: {current_date}")

# 4. 날짜 객체 만들기 (date(year, month, day))
custom_date = datetime.date(2022, 12, 25)
print(f"4. 특정 날짜: {custom_date}")

# 5. 시간 객체 만들기 (time(hour, minute, second))
custom_time = datetime.time(14, 45, 30)
print(f"5. 특정 시간: {custom_time}")

# 6. 날짜와 시간의 차이 계산 (timedelta)
date1 = datetime.date(2024, 10, 1)
date2 = datetime.date(2024, 10, 18)
date_diff = date2 - date1
print(f"6. 날짜 차이: {date_diff.days}일")

# 7. 시간을 더하거나 빼기 (timedelta)
ten_days_later = current_datetime + datetime.timedelta(days=10)
print(f"7. 10일 후의 날짜와 시간: {ten_days_later}")
five_hours_earlier = current_datetime - datetime.timedelta(hours=5)
print(f"7. 5시간 전의 날짜와 시간: {five_hours_earlier}")

# 8. 날짜와 시간 형식 지정하여 문자열로 변환 (strftime)
formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
print(f"8. 포맷된 날짜와 시간: {formatted_datetime}")

# 9. 문자열을 날짜/시간 객체로 변환 (strptime)
date_string = "2023-05-17 15:30:45"
parsed_datetime = datetime.datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
print(f"9. 문자열을 datetime 객체로 변환: {parsed_datetime}")

# 10. 시간대 정보를 포함한 현재 시간 (timezone-aware datetime)
utc_now = datetime.datetime.now(datetime.timezone.utc)
print(f"10. UTC 시간: {utc_now}")

# 11. 주의 시작일과 끝일 구하기
today = datetime.date.today()
start_of_week = today - datetime.timedelta(days=today.weekday())
end_of_week = start_of_week + datetime.timedelta(days=6)
print(f"11. 이번 주 시작일(월요일): {start_of_week}, 이번 주 마지막일(일요일): {end_of_week}")

# 12. pytz를 사용한 시간대 변환
# 'Asia/Seoul' 시간대에서 현재 시간을 구합니다.
seoul_tz = pytz.timezone('Asia/Seoul')
seoul_time = datetime.datetime.now(seoul_tz)
print(f"12. 서울 시간: {seoul_time}")

# 'US/Eastern' 시간대에서 현재 시간을 구합니다.
us_eastern_tz = pytz.timezone('US/Eastern')
us_eastern_time = datetime.datetime.now(us_eastern_tz)
print(f"12. 미국 동부 시간: {us_eastern_time}")

# 13. UTC 시간대를 특정 지역 시간대로 변환하기
# UTC 시간을 'Europe/London' 시간대로 변환
utc_time = datetime.datetime.now(pytz.utc)
london_tz = pytz.timezone('Europe/London')
london_time = utc_time.astimezone(london_tz)
print(f"13. UTC에서 런던 시간대로 변환: {london_time}")

# 14. 기존 naive datetime을 timezone-aware로 변환
# naive datetime 객체 (시간대 정보가 없는 시간) 생성
naive_datetime = datetime.datetime(2023, 10, 18, 12, 0, 0)
print(f"14. Naive datetime: {naive_datetime}")

# 'Asia/Seoul' 시간대를 추가하여 timezone-aware datetime으로 변환
aware_datetime = seoul_tz.localize(naive_datetime)
print(f"14. 시간대가 추가된 timezone-aware datetime (서울 시간): {aware_datetime}")

# 15. 두 시간대 간의 시간 차이 계산
# 서울 시간과 뉴욕 시간의 차이를 계산
new_york_tz = pytz.timezone('America/New_York')
new_york_time = aware_datetime.astimezone(new_york_tz)
print(f"15. 서울 시간 {aware_datetime} => 뉴욕 시간 {new_york_time}")
