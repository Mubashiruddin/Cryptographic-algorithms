a=input("enter the text : ")
k=input("enter the key : ")
a=a.replace(" ","")
print(a)
l3=list(a)
l4=list(k)
i=0
j=0
temp=0
for j in range (0,len(l3)):
    print(l4[i] , end="")
    if(i==(len(l4)-1)):
        i=0
    else:
        i=i+1
    j=temp+i
print("\n")

l1=[]
l2=[]
text=""
for i in k :
    l1.append((ord(i)-97))
def choose(n):
    if(n==1):
        return l1
    else:
        for i in l1:
            l2.append(-i)
        return l2
n1=int(input("enter choice 1.encryption 2.decryption"))
l=choose(n1)
j=0;
for i in a:
    if(ord(i)>96):
        temp=chr((ord(i)+l[j]-97)%26+97)
    else:
        temp=chr((ord(i)+l[j]-65)%26+65)
    text=text+temp
    j=j+1
    if(j%len(k)==0):
        j=0
print(text)