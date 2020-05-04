<<<<<<< HEAD
num = input("Enter number: ")
ch = input("Enter char: ")

   
   if(num%2 == 1)
   {
       for (i=0; i<=num/2; i++) //rows
       {
           for(j=0; j<num/2-i; j++) //backspace
           {
               cout<<" ";
           }
           for( j=0; j<2*i+1; j++) //char
           {
               cout<<ch;
           }
           cout<<"\n";
       }
       
   }
   else
   {
       cout<<"wrong input\n";
   }
=======
num=int(input("Insert a number: "))
counter=2


while counter<num:
    if num%counter==0:
        break
    counter+=1


if counter==num:
    print("prime number")
else:
    print("not a prime number")
>>>>>>> e739772a5ee9a8e2c9775dfd593b53ef25373505
