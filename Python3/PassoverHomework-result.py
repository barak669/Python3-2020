ID = input("Enter your ID: ")

if (len(ID)>9):
  print('Sorry your ID is ti long')
else:
  ID='0'*(9-len(ID))+ID
  sum=0
  for x in range(0, len(ID)):
    temp=int(ID[x]) * (1+(x%2))
    sum+=temp%10 + temp//10

if sum%10==0:
  print('Your ID is valid')
else:
  print('your ID is not valid')

