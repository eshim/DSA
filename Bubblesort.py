x = [5,2,7,42,4,3]

def bubbleSort(seq):

    for passnum in range(len(seq)-1,0,-1):
        for i in range(passnum):
            if seq[i]< seq[i+1]:
                seq[i], seq[i+1] = seq[i+1], seq[i]

bubbleSort(x)
print(x)