class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        n = len(position)
        position.sort()
        
        def find_distance(distance):
            count, current = 1, position[0]
            for i in range(1, n):
                if position[i] - current >= distance:
                    count += 1
                    current = position[i]
                    if count >= m:
                        return True
            
            return False
        
        left, right = 1, position[-1] - position[0]
        
        while left <= right:
            mid = (left + right) // 2
            if find_distance(mid):
                left = mid + 1
            else:
                right = mid - 1
        
        return right
