def beauty_sum(S):
    total_beauty=0
    for i in range(len(S)):
        freq=[0]*26

        for j in range(i,len(S)):
            index=ord(s[j])-ord('a')
            freq[index]=freq[index]+1
            max_freq=0
            min_freq=float('inf')

            for count in freq:
                if count>0:
                    max_freq=max(max_freq,count)
                    min_freq=min(min_freq,count)
            total_beauty=total_beauty+(max_freq-min_freq)
    return total_beauty



S= "xyx"
print(beauty_sum(S))