A = [1,3,5,7,9]
B = [2,4,6,8,10]

def mergeTwoArray(A,B):
    i,j = 0, 0
    C = []
    while i < len(A) and j < len(B):
        if A[i] < B[j]:
            C.append(A[i])
            i += 1
        else:
            A[i] > B[j]
            C.append(B[j])
            j += 1
    while i < len(A):
        C.append(A[i])
        i += 1
    while j < len(B):
        C.append(B[j])
        j += 1
        
    return C

print(mergeTwoArray(A,B))