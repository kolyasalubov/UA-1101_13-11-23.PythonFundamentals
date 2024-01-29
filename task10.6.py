def change_class_name(old_name, new_name):
    if not old_name.isidentifier() or not old_name[0].isupper():
        raise ValueError("Invalid class name format. It should start with an uppercase letter and contain only alphanumeric characters.")
    
    if not new_name.isidentifier() or not new_name[0].isupper():
        raise ValueError("Invalid new class name format. It should start with an uppercase letter and contain only alphanumeric characters.")
    
    globals()[new_name] = globals().pop(old_name)

class MyClass:
    pass

change_class_name("MyClass", "UsefulClass")
print(UsefulClass)
