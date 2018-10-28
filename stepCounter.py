def main():
    posSteps = []
    n = 0
    while n < 2:
        n = int(input('Enter the number of stairs (n): '))

    while len(posSteps) < n:
        step = int(input('Enter a possible step to be taken(Enter 0 when done): ' ))
        if step == 0:
            if len(posSteps) >= 2:
                break
            else:
                print('Need at least 2 possible steps.')
                continue
                
        elif step in posSteps:
            print('Must be a new number')
            continue
        
        elif (step < 0) or (step > n):
            print('Must be between 1 and n')
            continue
        
        else:
          posSteps.append(step)

    posSteps.sort()
    countPaths(n, posSteps)


##Calculate n for all steps
def countPaths(n, posSteps):
    count = [0] * (n+1)

    ##increment steps by step % possible step
    for x in range(1, posSteps[-1] + 1):
        for y in range(0, len(posSteps)):
            if ((x % posSteps[y]) == 0):
                count[x-1] += 1
                
    ##add up initial steps to calculate later steps
    #for x in range(posSteps[len(posSteps)-1], n):
    for x in range(0, n):
        for y in range(0, len(posSteps)):
            print(count[x], "+", count[x-(posSteps[y])])
            count[x] += count[x-(posSteps[y])]

    ##print n for all steps
    for x in range(0, len(count)-1):
        print("stair",  x+1, " = ", count[x])

    ##prints only the given step
    #return count[n]

if(__name__ == "__main__"):
    main();
