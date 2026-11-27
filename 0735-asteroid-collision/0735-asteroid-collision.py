class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        stack = []
        for a in asteroids:
            while stack and a < 0 and stack[-1] > 0 and stack[-1] < -a:
                stack.pop()
            
            if stack and a < 0 and stack[-1] > 0:
                if stack[-1] == -a:
                    stack.pop()
                # If stack[-1] > -a, 'a' explodes, so do nothing
            else:
                stack.append(a)
                
        return stack
