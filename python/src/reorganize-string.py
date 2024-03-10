import heapq

# https://docs.python.org/3/library/collections.html#collections.Counter
from collections import Counter

class Solution:

    def reorganizeString(self, s:str) -> str:
        
        ans = []
        # Min heap ordered by character counts, so we will use
        # negative values for count
        pq = [(-count, char) for char, count in Counter(s).items()]
        heapq.heapify(pq)

        while pq:
            count_first, char_first = heapq.heappop(pq)
            if not ans or char_first != ans[-1]:
                ans.append(char_first)
                if count_first + 1 != 0: 
                    heapq.heappush(pq, (count_first + 1, char_first))
            else:
                if not pq: return ''
                count_second, char_second = heapq.heappop(pq)
                ans.append(char_second)
                if count_second + 1 != 0:
                    heapq.heappush(pq, (count_second + 1, char_second))
                heapq.heappush(pq, (count_first, char_first))

        return ''.join(ans)
    

test_string = "aabbcc"
p = Solution()
print(p.reorganizeString(test_string))


# dbdbdbdcdc
# dbdbdbdcdcc#
# c

