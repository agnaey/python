pro=[{'code':1,'name':'shirt','stock':21,'type':'cotten','rs':500}]
while True:
    print(
        '''
1.add product
2.view all product
3.remove product
4.Update product
5.search all product
6.exit
'''
    )
    ch=int(input('enter your choise:'))
    if ch==1:
        code=int(input('enter the code:'))
        name=input('enter the name:')
        stock=int(input('enter the stock avalibe:'))
        type=input('enter the type:')
        rs=int(input('enter the MRP:'))
        pro.append({'code':code,'name':name,'stock':stock,'type':type,'rs':rs})
    elif ch==2:
        print('{:<10}{:<20}{:<10}{:<20}{:<10}'.format('code','name','stock','type','rs'))
        print('-'*70)
        for i in pro:
            print('{:<10}{:<20}{:<10}{:<20}{:<10}'.format(i['code'],i['name'],i['stock'],i['type'],i['rs']))
    elif ch==3:
        code=int(input('enter the code:'))
        f=0
        for i in pro:
            if i['code']==code:
                f=1
                pro.remove(i)
        f==0
        print('code not found')
    elif ch==4:
        code=int(input('enter the code:'))
        f=0
        for i in pro:
            if i['code']==code:
                f=1
                while True:
                    print(

                        '''
1.update name
2.update stock
3.update type
4.update MRP
5.exit
'''

                    )
                    ch=int(input('enter your choise:'))
                    if ch==1:
                        new_name=input('enter new name:')
                        i['name']=new_name
                    elif ch==2:
                        new_stock=input('enter new stock:')
                        i['stock']=new_stock
                    elif ch==3:
                        new_type=input('enter new type')
                        i['type']=new_type
                    elif ch==4:
                        new_rs=input('enter new mrp:')
                        i['rs']=new_rs
                    elif ch==5:
                        break
                    else:print('invalid')
    elif ch==5:
        code=int(input('enter the code:'))
        f=0
        for i in pro:
            if i['code']==code:
                f=1
                print('{:<10}{:<20}{:<10}{:<20}{:<10}'.format('code','name','stock','type','rs'))
                print('{:<10}{:<20}{:<10}{:<20}{:<10}'.format(i['code'],i['name'],i['stock'],i['type'],i['type']))
    elif ch==6:
        break
    else:print('invalid')