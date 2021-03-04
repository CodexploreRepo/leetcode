class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        arraySize = len(prices)
        result = []
        for i in range(0, arraySize):
            flag = True
            sale = prices[i]
            for j in range(i+1, arraySize):
                if prices[j] <= prices[i]:
                    sale = prices[i] - prices[j]
                    break
            result.append(sale)
        return result
        
