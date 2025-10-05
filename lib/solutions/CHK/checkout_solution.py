
class CheckoutSolution:

    # skus = unicode string
    # Specials: 3A for 130, 2B for 45

    def checkout(self, skus):
        totalCost = {}

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

        return totalCost



