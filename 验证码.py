def check_code():
    import random
    checkcode = ""
    for i in range(0,4):
        current = random.randint(0,4)
        if current != i:
            temp = chr(random.randrange(65,90))
        else:
            temp = random.randint(0,4)
        checkcode += str(temp)
    return checkcode




while True:
    code = check_code()
    print(code)
    usercode = input("请输入验证码").upper()
    if usercode == code:
        print("验证成功，欢迎登陆")
        break
    else:
        print("验证失败，请重新来")


