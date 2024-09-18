lib=[]

id=101
id_value = 101
def register():
    global id_value
    name=input('enter your name :')
    place=input('enter your place :')
    address=input('enter your address :')
    mobile=int(input('enter your mobile :'))
    password=input('enter your password :')
    lib.append({'id':id_value,'name':name,'place':place,'address':address,'mobile':mobile,'password':password})
    id_value +=1
    print('registered')
def login():
    username=input('enter username :')
    password=input('enter password :')


while True:
    print(
        '''
1.register
2.login
2.exit
'''
    )
    ch=int(input('enter your choice :'))
    if ch==1:
        register()
    elif ch==2:
        login()
    elif ch==3:
        break
        

