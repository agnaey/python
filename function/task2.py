lib=[{'id': 101, 'name': 'agnaey', 'email': 'a', 'address': 'aaa', 'mobile': 36345, 'password': '1234','book':[]}]
book=[{'id': 101, 'name': 'one piece', 'stock': 20, 'price': 2000},{'id': 102, 'name': 'naruto', 'stock': 15, 'price': 1500}]


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
        lib.append({'id':id,'name':name,'email':email,'address':address,'mobile':mobile,'password':password,'book':[]})
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
    print('{:<10}{:<20}{:<10}{:<10}'.format('id','name','stock','price'))
    print('-'*40)
    for i in book:
        print('{:<10}{:<20}{:<10}{:<10}'.format(i['id'],i['name'],i['stock'],i['price']))

def update_book():
    id=input('enter your id: ')
    f2=0
    for i in book:
        if i ['id']==int(id):
            f2=1
            name=(input('update books name: '))
            stock=int(input('update books stock: '))
            price=int(input('update books price: '))
            i['name']=name
            i['stock']=stock
            i['price']=price
            print('updated successfully')
    if f2==0:
        print('---------invalid id-------')


def delete_book():
        id=input('enter books id: ')
        f3=0
        for i in book:
            if i['id']==id:
                f3=1
            book.remove(i)
            print('-------REMOVED------')
        if f3==1:
            print('-----invalid id------')

def view_users():
    print('-'*50)
    print('{:<10}{:<10}{:<10}{:<10}'.format('id','name','email','address','mobile'))
    print('-'*50)
    for i in lib:
        print('{:<10}{:<10}{:<10}{:<10}'.format(i['id'],i['name'],i['email'],i['address'],i['mobile']))

def view_pro(user):
    # print(user)
    print('-'*50)
    print('{:<10}{:<10}{:<10}{:<10}'.format('id','name','email','address','mobile'))
    print('-'*50)
    print('{:<10}{:<10}{:<10}{:<10}'.format(user['id'],user['name'],user['email'],user['address'],user['mobile']))

def view_book():
    print('-'*50)
    print('{:<10}{:<20}{:<10}{:<10}'.format('id','name','stock','price'))
    print('-'*50)
    for i in book:
        print('{:<10}{:<20}{:<10}{:<10}'.format(i['id'],i['name'],i['stock'],i['price']))

def book_take(user):
    id=int(input('enter book id you want to add: '))
    f=0
    for i in book:
        if i['id']==id:
            f=1
            if i['stock']>0:
                user['book'].append(i['id'])
                i['stock']-=1
                print('----book added----')
            else:
                print('-----out of stock------')
    if f==0:
            print('-----id not found--------')

def return_book(user):
    id=int(input('enter book id you want to return: '))
    f=0
    for i in book:
        if i['id']==id and id in user['book']:
            f=1
            i['stock']+=1
            user['book'].remove(id)
            print('--------book returned-------')
        # else:
        #     print('-----book id invalid-----')
    if f==0:
        print('-----book not found------')

def book_in_hand(user):
    print(user['book'])



while True:
    print(
        '''
1.register
2.login
3.exit
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
5.view users
6.logout
'''
                )
                sub_ch=int(input('enter your choice: '))
                if sub_ch==1:
                    add_book()
                elif sub_ch==2:
                    view_book()
                elif sub_ch==3:
                    update_book()
                elif sub_ch==4:
                    delete_book()
                elif sub_ch==5:
                    view_users()
                else:
                    break
        elif f==2:
            # print('---------user login----------')
            while True:
                print('''
                      1.view profile
                      2.view book
                      3.book take
                      4.return book
                      5.book in hand
                      6.exit

''')
                sub_ch=int(input('enter your choise:'))
                if sub_ch==1:
                    view_pro(user)
                elif sub_ch==2:
                    view_book()
                elif sub_ch==3:
                    book_take(user)
                elif sub_ch==4:
                    return_book(user)
                elif sub_ch==5:
                    book_in_hand(user)
                else:break


        else:print('------invalid username or password-------')
    elif ch==3:
        break
        

