#Python program to count Occurrence of a character in a string
string=input("Enter the string: ")
char=input("Please enter the char to find frequency of ta character\n")
count=0
for i in range(len(string)):
    if(string[i]==char):
        count=count+1
print("The frequency of the ",char,"in the string is: ",count)
