class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # Edge cases: 1 row or string shorter than numRows
        if numRows == 1 or numRows >= len(s):
            return s
        
        # Track characters for each row
        rows = [''] * numRows
        current_row = 0
        going_down = False
        
        # Iterate through characters and change direction at top/bottom
        for char in s:
            rows[current_row] += char
            if current_row == 0 or current_row == numRows - 1:
                going_down = not going_down
            current_row += 1 if going_down else -1
            
        return ''.join(rows)