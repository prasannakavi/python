user={'username':'lucky','password':123}#taking data base
username=input('enter username please ...')
password=input('enter password please...')
if username != user['username'] :
    print('username is invalid')
else:
    print('username is valid')
if password != user['password']:
    print('password is incorrect')
else:
    print('password is valid')
