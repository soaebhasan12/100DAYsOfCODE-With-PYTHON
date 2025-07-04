# 007 Python Typing Type Hints and Arrows


# age: int
# name: str
# height: float
# is_human: bool


def police_check(age: int) -> bool:
    if age > 10:
        can_drive = True
    else:
        can_drive = False
    return can_drive

























































# if print(police_check("twelve")):             Erro
if police_check(12):
    print("You may pass")
else:
    print("Pay a fine.")