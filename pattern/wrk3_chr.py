# a=65
# for i in range (4):
#     for j in range (4):
#         print(chr(a),end="  ")
#     a+=1
#     print()
'''
A A A A 
B B B B 
C C C C 
D D D D 
'''

# for i in range(4):
#     a=65
#     for j in range(4):
#         print (chr(a),end="  ")
#         a+=1
#     print()


'''
A  B  C  D  
A  B  C  D  
A  B  C  D  
A  B  C  D  
'''

# for i in range (1,4):
#         a=65
#         for j in range (i):
#             print (chr(a),end="  ")
#             a+=1
#         print()

'''
A  
A  B  
A  B  C 
'''

# a=65
# for i in range (1,4):
#     for j in range (i):
#         print (chr(a-j),end="  ")
#     a+=1
#     print()

'''
A  
B  A  
C  B  A  
'''

# a=65
# for i in range (1,4):
#     for j in range (i):
#         print (chr(a),end="  ")
#     a+=1
#     print()

'''
A  
B  B  
C  C  C  
'''

a=65
for i in range (1,5):
    if i%2==0:
        for j in range (i):
            print(chr(a-j),end="  ")
        print()
    else:
        a=65
        for j in range (i):
            print(chr(a),end="  ")
            a+=1
        print()

'''
A  
B  A  
A  B  C  
D  C  B  A  
'''