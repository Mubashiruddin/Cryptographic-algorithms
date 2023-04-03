# ...Main code for initializing rails
rows=int(input("entr the no o rails : "))
text=input("enter the Text :")

c=len(text)
i=0
#enter q at end of string to complete matrix
while(i!=c):
    text=text+'q'
    #print("i1:",i)
    #print(len(a)%(2*b-2))
    i=i+1
    if(len(text)%(2*rows-2)==rows):
        i=c
        #print("i2:",i)
print(text)
rail=[]
for i in range(rows):
    rail.append([])
for i in text:
    for j in range(rows):
        rail[j].append('')
#print(rail)

#printing rails
def printlist(rails):
    for i in rails:
        print(i)

#adding the text in zig zag manner in the rails
k=0
row=0
flag=0
for i in text:
    rail[row][k]=i;
    if(row==rows-1):
        flag=1
    elif(row==0):
        flag=0
    if(flag==0):
        row+=1
    elif(flag==1):
        row-=1
    k=k+1
cipher=''
printlist(rail)

#printing cipher text
for i in rail:
    for j in i:
        cipher=cipher+j
print("the Cipher is : ",cipher)


x=len(cipher)
n=(x+rows-2)/(2*(rows-1))
n=int(n)
rail2=[]
rail3=[]
for i in range(rows):
    rail2.append([])
    rail3.append([])
for i in cipher:
    for j in range(rows):
        rail2[j].append('')
j=0
Y=len(cipher)
for i in range(Y):
    if(i==n or i==Y-n):
            j=j+1
    for k in range(1,rows-2):
           if(i==(n+k*(2*n-1))):
                j=j+1
    rail3[j].append(cipher[i])
k=0
i=0
j=0
visit=0
count=0


for j in range(Y): 
    rail2[i][j]=rail3[i][0]
    del rail3[i][0]
    if(i==rows-1):
        count=1
        #print('1',i)
    if(i==0):
        count=0
        #print('2',i)
    if(count==0):
        i=i+1
        #print('3',i)
    elif(count==1):
        i=i-1
        #print('4',i)
printlist(rail2)
for i in range(rows+1):
    print(" ")
    for j in range(i):
        print(rail2[j])