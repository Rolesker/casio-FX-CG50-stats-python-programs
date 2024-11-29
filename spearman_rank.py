x_array=[]
length=int(input("enter length "))
for i in range(length):
 temp=float(input("x enter value "+str(i+1)+" "))
 x_array.append(temp)
    
y_array=[]
for i in range(length):
 temp=float(input("y enter value "+str(i+1)+" "))
 y_array.append(temp)

def find_largest(arr):
 largest=0.0
 for i in arr:
  if i>largest:
   largest=i
 return largest

def ranker(arr):
 ranked_array=[]
 for i in range(len(arr)):
  ranked_array.append(0)
 value_to_place=1
 done=False
 while done==False:
  add_this_time=0
  largest=find_largest(arr)
  if largest==0:
   done=True
  for i in range(len(arr)):
   if arr[i]==largest:
    ranked_array[i]=value_to_place
    arr[i]=-1
    add_this_time+=1
    value_to_place+=add_this_time
 return ranked_array

ranked_x_array=ranker(x_array)
print("RANKED X:")
print(ranked_x_array)
ranked_y_array=ranker(y_array)
print("RANKED Y:")
print(ranked_y_array)

d_squared_list=[]
for i in range(length):
 d_squared_list.append((ranked_x_array[i]-ranked_y_array[i])**2)
print("D SQUARED:")
print(d_squared_list)

sigma_d=0
for i in d_squared_list:
 sigma_d+=i

numerator=6*sigma_d
denominator=length*((length*length)-1)

print(1-(numerator/denominator))
