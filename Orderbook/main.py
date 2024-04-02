import heapq

def validate_init(func):
    """
    Decorator to validate parameters passed to the __init__ method of a class.
    This decorator ensures that the arguments passed to the __init__ method meet certain criteria.
    Args:
    - func: The original __init__ method.
    Returns:
    - wrapper: The wrapper function that performs the validation before calling the original __init__ method.
    """
    def wrapper(instance, user_id, amount, price , side):
        """
        Wrapper function.
        Args:
        - instance: The instance of the class.
        - user_id: The user ID (int64).
        - amount: The order quantity(int64).
        - price: The price in USD(int64).
        - side: The side of the order (0 for buy, 1 for sell) (bool).
        Returns:
        - result of calling the original __init__ method with validated parameters.
        """
        if amount <= 0:
            raise ValueError("Amount must be > 0")
        if price < 0:
            raise ValueError("Price must be >= 0")
        if side not in (0, 1):
            raise ValueError("Side must be 0 (buy) or 1 (sell)")
        return func(instance, user_id, amount, price, side)
    return wrapper

class Order:
    @validate_init
    def __init__(self, user_id, amount, price, side):
        """
        Class representing a single order
        @param side: 0=buy, 1=sell
        @param amount: order quantity
        @param price: price in USD
        @param user_id: user ID        
        """
        self.user_id = user_id
        self.amount = amount
        self.price = price
        self.side = side

    def __str__(self) -> str:
        return f"Order(user_id={self.user_id}, amount={self.amount}, price={self.price}, side={self.side})"

class Orderbook:
    def __init__(self):
        """
        class representing a single orderbook
        @param bids: dict of bids, price -> list of orders
        @param asks: dict of asks, price -> list of orders
        @param bid_heap: heap(list) with sorting bids
        @param ask_heap: heap(list) with sorting asks
        """
        self.bids = {} 
        self.asks = {} 
        self.bid_heap = [] 
        self.ask_heap = [] 

    def add_order(self, order:Order):
        """"
        Add an order to the orderbook.
        @param order: order to be added
        """
        if order.side:
            self._add_order(order, self.asks, self.ask_heap, True)
        else:
            self._add_order(order, self.bids, self.bid_heap, False)

    def _add_order(self, order, order_dict, order_heap, way):
        """
        Add an order to the order book and sort the heap accordingly.

        @param order: The order to be added.
        @param order_dict: The dictionary storing orders by price.
        @param order_heap: The heap representing the order book.
        @param way: A boolean flag indicating the sorting direction (True for ascending, False for descending).
        """
        price = order.price
        if price not in order_dict:
            order_dict[price] = []
            heapq.heappush(order_heap, price)
        if order not in order_dict[price]:
            order_dict[price].append(order)
            self._sort_heap(order_heap, way)
            #print(order_heap)

    def _sort_heap(self, heap, way):
        """"
        Sort the heap according to accending or descending order 
        @param heap: The heap to be sorted.
        @param way: A boolean flag indicating the sorting direction (True for ascending, False for descending).
        """
        heap.sort() if way else heap.sort(reverse=True)

   
    def update_order(self, ask_order, bid_order, trade_amount):
        """
        Update the order quantities after a trade.
    
        @param ask_order: The ask order in the trade.
        @param bid_order: The bid order in the trade.
        @param trade_amount: The amount traded.
    """
        ask_order.amount -= trade_amount
        bid_order.amount -= trade_amount

    def pop_order(self, order):
        """
        Remove the first order from the list.
    
        @param order: The order to remove.
        """
        order.pop(0)

    def delete_order(self, orders_dict, orders_heap, order_price):
        """
        Update the orders dictionary and heap by removing the price level if there are no more orders at that level.
        @params orders_dict: The dictionary containing orders at different price levels.
        @params orders_heap: The heap containing the price levels.
        @params order_price: The price level to be removed if there are no orders at that level.
        """
        if not orders_dict[order_price]:
            del orders_dict[order_price]
            heapq.heappop(orders_heap)

    def match_orders(self):
        """
        Match buy and sell orders in the order book until there are no more matching orders.
        """
        while self.bid_heap and self.ask_heap:
            lowest_ask = self.ask_heap[0]
            highest_bid = self.bid_heap[0]

            if lowest_ask <= highest_bid:
                ask_orders = self.asks[lowest_ask]
                bid_orders = self.bids[highest_bid]

                while ask_orders and bid_orders:
                    ask_order = ask_orders[0]
                    bid_order = bid_orders[0]

                    trade_amount = min(ask_order.amount, bid_order.amount)
                    trade_price = ask_order.price
                    self.print_execute_trade(ask_order.user_id, bid_order.user_id, trade_amount, trade_price)

                    self.update_order(ask_order, bid_order, trade_amount)

                    if ask_order.amount == 0:
                        self.pop_order(ask_orders)
                    if bid_order.amount == 0:
                        self.pop_order(bid_orders)

                self.delete_order(self.asks, self.ask_heap, lowest_ask)
                self.delete_order(self.bids, self.bid_heap, highest_bid)
            else:
                break

    def print_execute_trade(self, ask_user_id: int, bid_user_id: int, amount: int, price: int) -> None:
        # Print balance changes
        print(f"BalanceChange for user {ask_user_id}: {-amount * price} UAH")
        print(f"BalanceChange for user {bid_user_id}: {amount * price} UAH")

    def print_heap(self) -> None:
        # The function print all information about current orderbook
        print("\nBids Heap:")
        for price, orders in self.bids.items():
            print(f"Price: {price}, Orders: {[str(order) for order in orders]}")
            
        print("\nAsks Heap:")
        for price, orders in self.asks.items():
            print(f"Price: {price}, Orders: {[str(order) for order in orders]}")

        print(f"\nBids: {self.bid_heap}")
        print(f"Asks: {self.ask_heap}")


if __name__ == "__main__": 
    print("--------------------test1--------------------")
    order_book = Orderbook()
    # Add buy order
    order_book.add_order(Order(user_id=1, amount=10, price=25, side=False))
    order_book.add_order(Order(user_id=5, amount=10, price=35, side=False))
    # Add sell order
    order_book.add_order(Order(user_id=2, amount=50, price=30, side=True))
    order_book.add_order(Order(user_id=3, amount=10, price=32, side=True))
    order_book.add_order(Order(user_id=4, amount=5, price=3, side=True))
    order_book.match_orders()
    order_book.print_heap()

    print("--------------------test2--------------------")
    book2 = Orderbook() # test with duplicate
    # Add buy order
    book2.add_order(Order(user_id=1, amount=10, price=25, side=False))
    book2.add_order(Order(user_id=5, amount=10, price=25, side=False))
    # Add sell order
    book2.add_order(Order(user_id=2, amount=50, price=30, side=True))
    book2.add_order(Order(user_id=3, amount=10, price=32, side=True))
    book2.add_order(Order(user_id=4, amount=52, price=3, side=True))
    book2.match_orders()
    book2.print_heap()

    print("--------------------test3--------------------")
    book3 = Orderbook() # test with no matches
    # Add buy order
    book3.add_order(Order(user_id=1, amount=1, price=2, side=False))
    book3.add_order(Order(user_id=5, amount=10, price=5, side=False))
    # Add sell order
    book3.add_order(Order(user_id=2, amount=50, price=30, side=True))
    book3.add_order(Order(user_id=3, amount=10, price=32, side=True))
    book3.add_order(Order(user_id=4, amount=52, price=31, side=True))
    book3.match_orders()
    book3.print_heap()

    print("--------------------test4--------------------")
    book4 = Orderbook() # test with incorrect order
    try:
        book4.add_order(Order(user_id=3, amount=0, price=3, side=False))
    except ValueError as e:
        print("Error:", e)
    