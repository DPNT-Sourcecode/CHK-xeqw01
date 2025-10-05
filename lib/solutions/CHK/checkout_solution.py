
class CheckoutSolution:

    # skus = unicode string
    # Specials: 3A for 130, 2B for 45

    def checkout(self, skus):
        total_cost = 0

        prices = {
            'A': 50,
            'B': 30,
            'C': 20,
            'D': 15
        }

        offers = {
            'A' : (3, 130),
            'B' : (2, 45) 
        }

        if not isinstance(skus, str):
            return -1
        
        for ch in skus:
            if ch not in prices:
                return -1
            
        counts = {}
        for ch in skus:
            counts[ch] = counts.get(ch, 0) + 1

        for item, count in counts.items():
            if item in offers:
                offer_qty, offer_price = offers[item]
                offer_sets = count // offer_qty
                remainder = count % offer_qty
                total_cost += offer_sets * offer_price + remainder * prices[item]
            else:
                total_cost += count * prices[item]

        return total_cost





