def class_name_changer(cls, new_name):
    assert new_name[0].isupper() and new_name.isalnum(),\
            "Error! Wrong characters in the name."
    cls.__name__ = new_name