def new_password(oldpassword,newpassword):
    if newpassword != oldpassword and len(newpassword) >= 6:
        return True
    else:
        return False

oldpassword = 'Welkom123'
newpassword = (input('Wat wordt je nieuwe wachtwoord? '))
res = new_password(oldpassword,newpassword)
print(res)

