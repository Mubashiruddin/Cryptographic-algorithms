#plain stores plain text
#key stores key value
plain=input("enter the text : ")
key=input("enter the key : ")

#removing whitespaces from plain text
plain=plain.replace(" ","")
print(plain)

#storing plain text and key in lists'''
l3=list(plain)
l4=list(key)

#i and j are counting variables
i=0
j=0
temp=0

#now we print the stripped plain text and repeating key below it
for j in range (0,len(l3)):
    print(l4[i] , end="")
    if(i==(len(l4)-1)):
        i=0
    else:
        i=i+1
    j=temp+i
print("\n")

#initializing lists for encryption and decryption
l1=[]
l2=[]
text=""
for i in key :
    l1.append((ord(i)-97))

#This function acts like a switch statement for en and decryption
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

#major and common logic for encryption and decryption
for i in plain:
    if(ord(i)>96):
        temp=chr((ord(i)+l[j]-97)%26+97)
    else:
        temp=chr((ord(i)+l[j]-65)%26+65)
    text=text+temp
    j=j+1
    if(j%len(key)==0):
        j=0
print(text)