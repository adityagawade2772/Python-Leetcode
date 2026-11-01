class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        stack = []
        for i in range(0, len(asteroids)):
            if asteroids[i]>0:
                stack.append(asteroids[i])
            else:
                while len(stack) != 0 and stack[-1] < abs(asteroids[i])  and stack[-1]>0:
                    stack.pop()
                if len(stack) != 0 and stack[-1]==abs(asteroids[i]):
                    stack.pop()
                elif len(stack) ==0 or stack[-1] <0:
                    stack.append(asteroids[i])
        return stack

                

        