##added exception handling on choise

pro=[]
while True:
    print(
        '''
1.add cloths
2.view cloth details
3.update stocks
4.delete stocks
5.exit
'''
    )
    while True:
        try:
            ch=int(input('enter your choice :'))
            break
        except:
            print('----enter correct data----' )

        

    if ch==1:
        code=int(input('enter the code : '))
        name=input('enter the cloth name :')
        stock=int(input('enter avalible stocks :'))
        place=input('enter the place of origin :')
        type=input('enter the type of cloth: ')
        pro.append({'code':code,'name':name,'stock':stock,'place':place,'type':type})
    elif ch==2:
        print('{:<10}{:<20}{:<10}{:<20}{:<15}'.format('code','name','stock','place','type'))
        print('-'*70)
        for i in pro:
            print('{:<10}{:<20}{:<10}{:<20}{:<15}'.format(i['code'],i['name'],i['stock'],i['place'],i['type']))
    elif ch==3:
        code=int(input('enter cloth code: '))
        f=0
        for i in pro:
            if i['code']==code:
                f=1
                while True:
                    print(
                        '''

1.update stock
2.update place
3.update type
4.exit
'''
                    )
                    while True:
                        try:
                            ch=int(input(' enter your choise : '))
                            break
                        except:
                            print('----enter data correctly----')
                    if ch==1:
                        new_stock=int(input('enter the new stock:'))
                        i['stock']=new_stock
                    elif ch==2:
                        new_place=input('enter the new place: ')
                        i['place']=new_place
                    elif ch==3:
                        new_type=input('enter new type: ')
                        i['type']=new_type
                    elif ch==4:
                        break
                    else:print('invalid')
    elif ch==4:
        code=int(input('enter the code :'))
        f=0
        for i in pro:
             if i['code']==code:
                f=1
                pro.remove(i)
        if f==0:
            print('code not found')
    # elif ch==5:
    #     code=int(input('enter the code :'))
    #     f=0
    #     for i in pro:
    #         if i['code']==code:
    #             f=1
    #             print('{:<10}{:<20}{:<10}{:<20}{:<15}'.format('code','name','stock','place','type'))

    #             print('{:<10}{:<20}{:<10}{:<20}{:<15}'.format(i['code'],i['name'],i['stock'],i['place'],i['type']))

    elif ch==5:
        break
    else:print('invalid number') 
                

