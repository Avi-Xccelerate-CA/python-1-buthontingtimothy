# week 0 problem 1
# create a function that returns a list of (vitamins,injections) tuples for each attribute that they need.
# Complete problem statement in README.mds


# your input type should be a list,
# output should also be a list containing tuples
# Example:
# input: [250, 0, 250, 0, 0, 0]
# expected output: [(25,0),(0,0),(25,0),(0,0),(0,0),(0,0)]
# input: [500, 1, 2, 3, 4, 5]
#expected output: "No medicine given"
# HINT: using % operator to find remainder may be helpful
def dose(needs):
    #YOUR SOLUTION STARTS HERE
    # check total exceed 500 or not
    if sum(needs) >= 500:
        return "No medicine given"
    
    for item in needs:
        if item >= 250:
            return "No medicine given"
        
    solution = []
    for i in range(len(needs)):
        vit = needs[i] // 10
        inj = needs[i] % 10
        att = vit + (inj != 0), (10 - inj) * (inj != 0)
        solution.append(att)
    return solution
    #YOUR SOLUTION ENDS HERE
