import heapq

def find_maximize_capital(N, C, gains, prices):
    """
    The maximize_capital function takes in the number of laptops to buy, the initial capital,
    the gains array and prices array. It returns the maximum amount of money that can be made 
    by buying N laptops with C dollars.
    
    :param N: Specify the number of laptops that can be bought
    :param C: Represent the initial capital
    :param gains: Store the gains of each laptop
    :param prices: Store the prices of laptops
    :return: The maximum amount of capital that can be earned after buying n laptops
    """
    laptops = [(-gains[i], prices[i], i) for i in range(len(gains))] 
    heapq.heapify(laptops) 

    capital = C
    bought_laptops = 0

    while laptops and bought_laptops < N:
        gain, price, index = heapq.heappop(laptops) 
        gain = -gain 
        if capital >= price:
            capital -= price
            capital += gain
            bought_laptops += 1
    return capital

if __name__ == "__main__":
    N = int(input("Enter the number of laptops to consider (N): "))
    C = float(input("Enter the initial capital (C): "))
    gains = list(map(float, input("Enter the gains array: ").split()))
    prices = list(map(float, input("Enter the prices array: ").split()))

    final_capital = find_maximize_capital(N, C, gains, prices)
    print("Student's capital at the end of the summer:", final_capital)
