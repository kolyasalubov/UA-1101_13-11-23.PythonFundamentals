import logging


class OutOfWeekError(Exception):
    """number not in 1..7 range"""

    def __init__(self, data):
        self.data = data

    def __str__(self):
        return repr('Only 1..7 integers correspond to the days of the weeek')
    

def numberToDay(number):

    days_of_week_dict = {num: day for (num, day) in \
        list(enumerate(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'], 1))}
    if not number in days_of_week_dict.keys():
        logger.error(f'Input number out of required range: {number} ')
        raise OutOfWeekError('Days of the week must correspond to 1..7')
    return f'{number}: {days_of_week_dict[number]}'
    


logger = logging.getLogger(__name__)
w_handler = logging.StreamHandler()
f_handler = logging.FileHandler(r'HolubetsYustyna\HW11\hw11.2\days_of_week.log')
w_handler.setLevel(logging.WARNING)
f_handler.setLevel(logging.ERROR)

short_time_format = '%H:%M:%S'
w_format = logging.Formatter('%(asctime)s --> %(levelname)s --> %(message)s', datefmt=short_time_format)
f_format = logging.Formatter('%(asctime)s --> %(name)s --> %(levelname)s --> %(message)s ')
w_handler.setFormatter(w_format)
f_handler.setFormatter(f_format)

logger.addHandler(w_handler)
logger.addHandler(f_handler)



try:
    inp_number = int(input('Enter a number from 1 to 7: '))
    print(numberToDay(inp_number))
except OutOfWeekError as e:
    print(f'OutOfWeekError: {e.data}')
except TypeError as e:
    print(f'TypeError: {e}')
except SyntaxError as e:
    print(f'Syntax Error: e')
except KeyError as e:
    print(f'KeyError {e}')
except ValueError as e:
    print(f'ValueError: {e}')
else:
    logger.warning(f'Executed successfully')
finally:
    logger.warning(f'Finished execution')
