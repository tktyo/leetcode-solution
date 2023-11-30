# happy Number
class Solution:
    def isHappy(self, n: int) -> bool:
        table = {n}
        while n != 1:
            n = self.getSum(n)
            temp = len(table)
            table.add(n)
            if temp == len(table):
                return False
        return True

    def getSum(self, n: int) -> int:
        sum = 0
        while n:
            sum += (n % 10) * (n % 10)
            n //= 10
        return sum
