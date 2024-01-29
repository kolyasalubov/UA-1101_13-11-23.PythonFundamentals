philosophy = """
FIND SEPARATELY THE NUMBER OF OCCURRENCES OF THE WORDS
"BETTER", "NEVER" AND "IS" IN THE GIVEN LINE
YOU NEED TO DISPLAY ALL TEXT IN UPPERCASE (ALL LETTERS IN UPPERCASE)
REPLACE ALL OCCURRENCES OF THE SYMBOL "1" WITH "&"
"""

better_count = philosophy.upper().count("BETTER")
never_count = philosophy.upper().count("NEVER")
is_count = philosophy.upper().count("IS")

modified_philosophy = philosophy.replace('1', '&').upper()

print(f"Occurrences of 'BETTER': {better_count}")
print(f"Occurrences of 'NEVER': {never_count}")
print(f"Occurrences of 'IS': {is_count}")
print(f"Modified Text:\n{modified_philosophy}")
