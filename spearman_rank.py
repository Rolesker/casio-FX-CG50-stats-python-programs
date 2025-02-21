x_array=[]
length=int(input("enter length "))
for i in range(length):
 temp=float(input("x enter value "+str(i+1)+" "))
 x_array.append(temp)
    
y_array=[]
for i in range(length):
 temp=float(input("y enter value "+str(i+1)+" "))
 y_array.append(temp)

def ranker(arr):
 sorted_ver=sorted(arr)
 score_association=dict.fromkeys(arr,-1)
 for i in range(len(sorted_ver)):
  if score_association[sorted_ver[i]]==-1:
   score_association[sorted_ver[i]]=i+1
 for i in range(len(arr)):
  arr[i]=score_association[arr[i]]
 return arr

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
