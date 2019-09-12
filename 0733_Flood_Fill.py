# Problem 733
# Date completed: 2019/09/12

# 84 ms
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        
        h = len(image)    # -> sr
        w = len(image[0]) # -> sc
        if sr > h-1 or sc > w-1: return image
        origColor = image[sr][sc]
        if origColor == newColor: return image
        # print(origColor,newColor,h,w)
        
        stack = [[sr,sc]]
        while stack:
            r,c = stack.pop()
            # print(len(stack),r,c, r>0,r<h-1,c>0,c<w-1)
            image[r][c] = newColor
            
            if r > 0   and image[r-1][c]==origColor: stack.append([r-1,c])
            if r < h-1 and image[r+1][c]==origColor: stack.append([r+1,c])   
            if c > 0   and image[r][c-1]==origColor: stack.append([r,c-1])
            if c < w-1 and image[r][c+1]==origColor: stack.append([r,c+1])
            # print(image)
        
        return image
        
