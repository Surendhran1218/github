class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        # Step 1: Find first and last occurrences of each character
        first = {}
        last = {}
        for i, ch in enumerate(s):
            if ch not in first:
                first[ch] = i
            last[ch] = i

        # Step 2: Find all minimal valid intervals
        valid_intervals = []
        for ch in first:
            l, r = first[ch], last[ch]
            possible = True
            
            # Expand interval to include all occurrences of any inner characters
            i = l
            while i <= r:
                if first[s[i]] < l:
                    # An inner character starts before 'l', invalid candidate starting at 'l'
                    possible = False
                    break
                r = max(r, last[s[i]])
                i += 1
            
            if possible:
                valid_intervals.append((l, r))

        # Step 3: Greedy interval selection based on end position
        valid_intervals.sort(key=lambda x: x[1])
        
        res = []
        last_end = -1
        for l, r in valid_intervals:
            if l > last_end:
                res.append(s[l:r + 1])
                last_end = r

        return res