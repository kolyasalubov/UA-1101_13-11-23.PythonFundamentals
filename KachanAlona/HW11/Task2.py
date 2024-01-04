dict_days = {
    1: 'Monday',
    2: 'Tuesday',
    3: 'Wednesday',
    4: 'Thursday',
    5: 'Friday',
    6: 'Saturday',
    7: 'Sunday'
}


def day_from_num():
    try:
        num = int(input('Write a number: '))
        if num < 0 or num > 8:
            raise ValueError('Number should be beetwen 1 to 7')
    except ValueError as e:
        print(e)

    else:
        print(dict_days.get(num))


day_from_num()
