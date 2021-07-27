def main():
    user_email = "sstreger@volstate.edu"
    is_valid_email(user_email)
    print(is_valid_email(user_email))
    # print true or false depending on result of function


def is_valid_email(user_email):
    spec_char = '@'
    edu = '.edu'
    has_char = False
    has_edu = False
    if spec_char in user_email:
        if edu in user_email:
            has_char = True
            has_edu = True
        else:
            has_char = False
            has_edu = False
    if has_char and has_edu:
        is_valid = True
    else:
        is_valid = False

    return is_valid

main()