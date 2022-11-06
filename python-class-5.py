a=int(input())
b=int(input())
sum=a+b
print(sum)




#-------------------------------------------
import math
a= min(1,2,3)
b= max(1,2,3)
c=math.floor(2.1)
d=math.ceil(2.1)
print(c)
print(d)



#------------------------------------------



student=["ram","shayam","harjas"]
#for i in "anurag": 
for i in student: 
   if i == "harjas":
    # break
    continue
                         #for i in student: 
print(i)




#-------------------------------------------------




student=["anurag","sunil","ram"]
color=["red","yello","pink"]    
for i in student:
    for j in color:
        print(i,j)



 #----------------------------------
 # 
 # 
 # 
 #         
a={"anurag","sunil","ram"}
#for i in a:
a.add("eyy")

print(a)


#-----------------------------------------


a={
    "name":"anurag",
    "company":"microsoft",
    "collage":"lovely"
}
#print(a)
a["degree"]="engineering"
if "name" in a:
    print("yes it exists")





#--------------------------------------------------------------------


x=10
y=20
x,y=y,x
print(x,y)




a=str(input())
b=str(input())
c=ord(a[0])
d=ord(b[0])
#c+=d






print("c+=d","c=",c+d,"d=",a)
a=int(input())
if(a%2==0):
    print("p")
elif(a%2==1):
    print("n")
else:
    print("None")  
#






t= 1


while True:
    if(t % 2 != 0):
       print("tihs is true")
       break
    print(t)
    t += 1
#---------------------------



z = 54.19
print("%5.2f"%z)
#---------------------------



print(22 % 3)
#--------------------------



#question

c_o_d = 222,4,44

c o d = 2000 3000 4000

 
# ---------------------------
k = complex(2, 3)
print(k)

j = 2 + 3j
print(j)

#---------------------------



print(19 // 4)
#---------------------------






print(3 ^ 4)
#---------------------------



x = 2 ** 3 + 9 * ((3 * 12) - 8) / 10
print(x)



#------------------------------


print(2 ** 3)
#---------------------------


print('{0:.2f}'.format(1.234))
#---------------------------


x = "high"
x = x + "3"
print(x * 3)
#---------------------------








for ct in range(10):
    if(ct == 6):
        break
    else:
        print(ct, end = " ")

else:
    print("code", end = " ")
def pr():
    print("i am yours ")
pr()  # Function::- a function is a group of related statements that performs a specific task.
def pr(name):
    print("chiper "+name)
pr('school')    
def pr(first_name,last_name):
   print(first_name+" "+last_name)
pr('jai','raj') 








#-------------------------

def pr(* name):
   print("my name is " + name[2])
pr("hgjhgj","gfhgf","school")
def pr(name):
    for i in name:
        print(name)
name=['ram','ahyam','hero']
pr(name)   
 

 #----------------------------------
 
def pr(n):
    return 5 * n
    
a = pr(9)
print(a) 
###recursion on factoriyal  
  
def factoriyal(n):
    if n ==1:
        return 1
    else:return(n*factoriyal(n-1))
factoriyal(5)


#----------------------------



def sum(n):
    if n<=1:
       return n
    else:
        return n + sum(n-1)
n=5          