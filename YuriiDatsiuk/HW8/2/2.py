import string


def correct_password(user_password):
    result = True

    if len(user_password) < 6:
        print(f'password must have minimum 6 symbols')
        result = False
    elif len(user_password) > 16:
        print(f'password must have maximum 16 symbols')
        result = False
    else:
        list_spec_symbols = ['$','#','@']
        list_numbers = [chr(x) for x in range(ord('0'), ord('9')+1)]
        list_az = string.ascii_lowercase
        list_AZ = string.ascii_uppercase

        result_spec = result_num = result_low = result_upp = False

        for symbol in user_password:
            if not result_spec:
                result_spec = True if symbol in list_spec_symbols else False
            if not result_num:
                result_num  = True if symbol in list_numbers else False
            if not result_low:
                result_low  = True if symbol in list_az else False
            if not result_upp:
                result_upp  = True if symbol in list_AZ else False

        if not result_spec:
            print(f'must have one symbols in - ',list_spec_symbols)
        if not result_num:
            print(f'must have one symbols in - ',list_numbers)
        if not result_low:
            print(f'must have one symbols in - ',list_az)
        if not result_upp:
            print(f'must have one symbols in - ',list_AZ)

        result = result_spec and result_num and result_low and result_upp

    return result

user_password = input("write password ")
result = correct_password(user_password)
print('correct' if result else 'not correct')