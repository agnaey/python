# l=['helo','apple','welcome','python','hweqweqw','malayalam','amma']
# rev=0
# for i in  l:
#     if i==i[::-1]:
#         print(i)




l=['helo','apple','welcome','python','hweqweqw','malayalam','amma']
for i in l :
    k=0
    for j in i :
        f=0
        if i[k]==i[len(i)-k-1]:
            k+=1
        else:
            f=1
            break
    if f==0:
        print(i)

            

