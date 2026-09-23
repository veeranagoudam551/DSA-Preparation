class Solution(object):
    def maxScore(self, cardPoints, k):

        n = len(cardPoints)

        # Total sum of all cards
        total = sum(cardPoints)

        # Size of the window we leave behind
        window_size = n - k

        # If we take all cards
        if window_size == 0:
            return total

        # Sum of first window
        window_sum = sum(cardPoints[:window_size])

        min_window = window_sum

        # Slide the window
        for i in range(window_size, n):

            window_sum = window_sum - cardPoints[i - window_size]
            window_sum = window_sum + cardPoints[i]

            min_window = min(min_window, window_sum)

        # Maximum cards taken
        return total - min_window