#Check for balanced parentheses in an expression
#This is a standard problem available on geeksforgeeks.org
#Link: https://www.geeksforgeeks.org/check-for-balanced-parentheses-in-an-expression/


#boolean function to find out if the brackets are balanced
def balanced(brackets):
    #split the string into individual characters
    exp = list(brackets)
    #we define an empty stack named st
    st = []     
    for i in range(0,len(exp)):
        #if its an opening bracket, push it to the stack
        if(exp[i]=='(' or exp[i]=='[' or exp[i]=='{'):
            a = exp[i]
            st.append(a)
        #if its a closing bracket
        else:
            if(exp[i]==')'):
                if(len(st)==0):
                    return 0
                else:
                    a = st.pop()
                    if(a=='[' or a =='{'):
                        return 0
            if(exp[i]==']'):
                if(len(st)==0):
                    return 0
                else:
                    a = st.pop()
                    if(a=='(' or a =='{'):
                        return 0
            if(exp[i]=='}'):
                if(len(st)==0):
                    return 0
                else:
                    a = st.pop()
                    if(a=='(' or a =='['):
                        return 0

    #if the string is processed and the stack is not empty return 0
    if(len(st)==0):
        return 1
    else:
        return 0


#main function
brackets = "{()}[]"
if(balanced(brackets)):
    print("Balanced!")
else:
    print("Not Balanced!")
