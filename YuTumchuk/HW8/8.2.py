password = "dfeyert4b45345134+"


def pasw_validation(some_input):
    import re
    sm_letters = re.findall("[a-z]", some_input)
    lg_letters = re.findall("[A-Z]", some_input)
    numms = re.findall("[0-9]", some_input)
    sp_symbols = re.findall("[$#@]", some_input)
    length = len(some_input)
    if not sm_letters:
        print("Add at least one small letter to your password")
    if not lg_letters:
        print("Add at least one large letter to your password")
    if not numms:
        print("Add at least one digit to your password")
    if not sp_symbols:
        print("Add at least one of this symbols - $,#,@ to your password")
    if length<6:
        print("Too short password, please re-type")
    if length > 16:
        print("Too long password, please re-type")


pasw_validation(password)
