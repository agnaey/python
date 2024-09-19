lib=[]
book=[]


def register():    
    email=input('enter your email :')
    f1=0
    for i in lib:
        if i['email']==email:
            f1=1
            print('------email already exits------')
            register()
    if f1==0:
        if len(lib)==0:
            id=101
        else:
            id=lib[-1]['id']+1
        print('your id: ',id)
        name=input('enter your name :')
        address=input('enter your address :')
        mobile=int(input('enter your mobile :'))
        password=input('enter your password :')
        lib.append({'id':id,'name':name,'email':email,'address':address,'mobile':mobile,'password':password})
        print('------registered------')
def login():
    username=input('enter username :')
    password=input('enter password :')
    f=0
    user=''
    if username=='admin' and password=='admin':
        f=1
    for i in lib:
        if username==i['email'] and password==i['password']:
            f=2
            user=i
    return f,user

def add_book():
    if len(book)==0:
        id=101
    else:
        id=book[-1]['id']+1
    print('book id:',id)
    name=input('enter book name: ')
    stock=int(input('enter the avalible stock: '))
    price=int(input('enter the prize: '))
    book.append({'id':id,'name':name,'stock':stock,'price':price})
    print('-------book added-------')

def view_book():
    print('{:<10}{:<10}{:<10}{:<10}'.format('id','name','stock','price'))
    print('-'*40)
    for i in book:
        print('{:<10}{:<10}{:<10}{:<10}'.format(i['id'],i['name'],i['stock'],i['price']))

# def update_book():
    # for i in book:
        # if i in ['id']==

# def delete_book():
#         id=input('enter your id: ')
#         f3=0
#         for i in emp:
#             if i['id']==id:
#                 f3=1
#             book.remove(i)
#             print('REMOVED!!!')
#         if f3==1:
#             print('invalid id')

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
        f,user=login()
        if f==1:
            # print('--------admin login---------')
            while True:
                print(
                    '''
1.add book
2.view book
3.update book
4.delete book
5.view book
'''
                )
                sub_ch=int(input('enter your choice: '))
                if sub_ch==1:
                    add_book()
                if sub_ch==2:
                    view_book()
                if sub_ch==3:
                    update_book()
                if sub_ch==4:
                    delete_book()
        elif f==2:
            print('---------user login----------')


        else:print('------invalid username or password-------')
    elif ch==3:
        break
        

