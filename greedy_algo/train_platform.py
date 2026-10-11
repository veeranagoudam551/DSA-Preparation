
class Solution:
    def findPlatform(self, arrival, departure):
        arrival.sort()
        departure.sort()

        i = 0
        j = 0
        platforms = 0
        max_platforms = 0
        n = len(arrival)

        while i < n:
            if arrival[i] <= departure[j]:
                platforms += 1
                max_platforms = max(max_platforms, platforms)
                i += 1
            else:
                platforms -= 1
                j += 1

        return max_platforms


arrival = [900, 940, 950, 1100, 1500, 1800]
departure = [910, 1200, 1120, 1130, 1900, 2000]

obj = Solution()
answer = obj.findPlatform(arrival, departure)

print("Minimum platforms required:", answer)
