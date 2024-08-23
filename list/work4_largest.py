l=['helo','apple','welcome','python','hweqweqw']
largest=l[0]
for i in l:
    if len(i)>len(largest):
        largest=i
print(largest)