'''Function to check if it is possible to cut the cake in the given way:
1. Cut the cake into N equal pieces.
2. Cut the cake into N pieces of any size.
3. Cut the cake into N pieces such that no two of them are equal.'''

def cutCake(N):
    # Case 1
    if(360%N==0):
        print("It is possible to cut the cake into",N,"equal pieces.\n");
    else:
        print("It is not possible to cut the cake into",N,"equal pieces.\n");   
    # Case 2
    if(N<=360):
        print("It is possible to cut the cake into",N,"pieces of any size.\n");
    else:
        print("It is not possible to cut the cake into",N,"pieces of any size.\n");
    # Case 3
    if(((N*(N+1))/2)<=360):
        print("It is possible to cut the cake into",N,"pieces such that no two of them are equal.\n");
    else:
        print("It is not possible to cut the cake into",N,"pieces such that no two of them are equal.\n");

N=int(input("N:"))
cutCake(N)

'''Case 1 will only be possible if 360 is divisible by n.
For Case 2 to be possible,n must be ≤ 360.
For Case 3 to be possible,(n*(n+1))/2 must be ≤ 360.'''
