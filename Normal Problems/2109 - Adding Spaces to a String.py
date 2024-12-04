class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str: #type:ignore
        final_list = []
        prev_index = 0 # to know where to start the indexing for each string

        for i in range(len(spaces)):
            final_list.append(s[prev_index:spaces[i]]) # adds all the letters from the prev_index to the current index
            prev_index = spaces[i] # update the prev_index to new index
            # print(final_list)  
        
        final_list.append(s[prev_index:])
        return " ".join(final_list)