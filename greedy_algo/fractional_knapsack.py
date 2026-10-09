class Solution:
    def fractionalKnapsack(self, val, wt, cap):
        items = []

        for i in range(len(val)):
            ratio = val[i] / wt[i]
            items.append((ratio, val[i], wt[i]))

        items.sort(reverse=True)

        total_value = 0.0

        for ratio, value, weight in items:
            if cap >= weight:
                total_value += value
                cap -= weight
            else:
                total_value += ratio * cap
                break

        return total_value


# Input
n = int(input("Enter number of items: "))

val = list(map(int, input("Enter item values: ").split()))
wt = list(map(int, input("Enter item weights: ").split()))

cap = int(input("Enter knapsack capacity: "))

# Solve
obj = Solution()
answer = obj.fractionalKnapsack(val, wt, cap)

print(f"Maximum value: {answer:.6f}")