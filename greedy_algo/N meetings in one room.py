
class Solution:
    def maxMeetings(self, start, end):
        meetings = []

        for i in range(len(start)):
            meetings.append((end[i], start[i]))

        meetings.sort()

        count = 0
        last_end = -1

        for finish, begin in meetings:
            if begin > last_end:
                count += 1
                last_end = finish

        return count

# Example input
start = [1, 3, 0, 5, 8, 5]
end = [2, 4, 6, 7, 9, 9]

obj = Solution()
print(obj.maxMeetings(start, end))
