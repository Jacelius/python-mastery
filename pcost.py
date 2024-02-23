def portfolio_cost(filename):
    total_cost = 0
    with open(filename, "r") as f:
        for line in f:
            split = line.split()
            try:
                num_shares = int(split[1])
                price = float(split[2])
                total_cost += num_shares*price
                
            except ValueError as e:
                print("Couldn't parse:", repr(line))
                print("Reason:", e)
    return total_cost
                
print(portfolio_cost('Data/portfolio3.dat'))