m=int(input("Enter table row length "))
n=int(input("Enter table column length "))

def table_former(length,height):
 table=[]
 for i in range(height+1):
  table.append([])
  for j in range(length+1):
   table[i].append(0)
 return table

def table_printer(table):
 for i in table:
  print(i)
 print()

def observed_table_filler(table):
 #forming
 for i in range(len(table)-1):
  for j in range(len(table[i])-1):
   table[i][j]="!"
   table_printer(table)
   replace_value=int(input("Enter the value to replace the !: "))
   table[i][j]=replace_value
 #horizontal total
 for i in range(len(table)-1):
  sum=0
  for j in range(len(table[i])):
   sum+=table[i][j]
   if j==len(table[i])-1:
    table[i][j]=sum
 #vertical total
 for i in range(len(table[0])):
  sum=0
  for j in range(len(table)):
   sum+=table[j][i]
   if j==len(table)-1:
    table[j][i]=sum
 #done
 print("OBSERVED VALUES:")
 table_printer(table)
 return table

def expected_table_former(observed_table):
 #inputting totals
 height=len(observed_table)
 length=len(observed_table[0])
 expected_table=[]
 for i in range(height):
  expected_table.append([])
  for j in range(length):
   expected_table[i].append(0)
   if j==length-1 or i==height-1:
    expected_table[i][j]=observed_table[i][j]
 #calculating expected values
 sample_size=observed_table[height-1][length-1]
 for i in range(height):
  horizontal_total=expected_table[i][length-1]
  for j in range(length):
   vertical_total=expected_table[height-1][j]
   expected_table[i][j]=round(float((vertical_total*horizontal_total)/sample_size),4)
 #checking for less than 5
 for i in range(len(expected_table)-1):
  for j in expected_table[i]:
   if j<5:
    print("ERROR: EXPECTED FREQUENCY LESS THAN 5 DETECTED, YOU SHOULD CONSIDER MERGING COLUMNS OR COLLECTING MORE DATA")
 #done
 print("EXPECTED VALUES:")
 table_printer(expected_table)
 return expected_table

def contingency_table_former(observed_table,expected_table):
 #table forming
 height=len(observed_table)
 length=len(observed_table[0])
 contingency_table=[]
 for i in range(height-1):
  contingency_table.append([])
  for j in range(length-1):
   contingency_table[i].append(0)
 #inputting contributing values
 for i in range(height-1):
  for j in range(length-1):
   contributing_value_numerator=(observed_table[i][j]-expected_table[i][j])**2
   contributing_value=float(contributing_value_numerator/expected_table[i][j])
   contingency_table[i][j]=round(contributing_value,4)
 print("CONTRIBUTING VALUES:")
 table_printer(contingency_table)
 #finding chi-squared
 chi_squared=0
 for i in range(len(contingency_table)):
  for j in contingency_table[i]:
   chi_squared+=j
 chi_squared=round(chi_squared,2)
 print("CHI SQUARED:")
 print(chi_squared)



basic=table_former(m,n)
observed=observed_table_filler(basic)
expected=expected_table_former(observed)
contingency_table_former(observed,expected)
print()
print("DEGREES OF FREEDOM:")
print((m-1)*(n-1))