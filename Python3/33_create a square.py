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