from datetime import datetime, timedelta

print('欢迎使用工作日计算器！\n以下输入请用阿拉伯数字表示、英文句点.号分隔\n')
start_date = input('开始日期：年. 月. 日 如：2022.1.1\n请输入：>>')
end_date = input('结束日期：年. 月. 日 如：2022.12.31\n请输入：>>')
rest_day = input('休息日，0 代表周日， 1，代表周一，以此类推。如：每周日和周六休息，用 0,6 表示，不休息，用 -1 表示）：\n请输入：>>')
holiday = int(input('节假日，这期间共有几天的节假日？\n'))
count = 0

start_date_array = start_date.split('.')
end_date_array = end_date.split('.')
rest_day_array = rest_day.split(',')

start_date_array = list(map(int, start_date_array))
end_date_array = list(map(int, end_date_array))
rest_day_array = list(map(int, rest_day_array))

start = datetime(start_date_array[0], start_date_array[1], start_date_array[2])
end = datetime(end_date_array[0], end_date_array[1], end_date_array[2])

day = start

for i in range((end - start).days):
    day = start + timedelta(days=i)
    weekday = day.weekday()
    query = weekday not in rest_day_array
    if query:
        count += 1

print('\n', '计算得到，不含开始日和结束日，', start_date, '到', end_date, '期间工作日共有', count - 2 - holiday, '天')
print('包含开始日和结束日，共有', count - holiday, '天')
