import numpy as np

from union_find import UnionFind

def generate_maze(width: int, height: int, box_size: int, line_width: int):
    '''
    Generate numpy 2-D array representing each pixel of screen
    '''
    
    def _adjacent_blocks(index: int):
        '''
        @arg index index of inner wall
          if index is odd, the wall is horizontal,
          and (index // 2) is the index of block which the wall is attached.
        @return indices of two blocks related to the wall
        '''
        is_horizontal = index & 1
        index >>= 1
        x = index // width
        y = index - x * width
        d = ((0, 1), (1, 0))[is_horizontal]
        nx, ny = x + d[0], y + d[1]
        if nx >= height or ny >= width: return None, None
        return (x * width + y), (nx * width + ny)

    def _build_spanning_tree():
        '''
        Randomly select indices of walls to remove,
        for connection of each blocks satisfying tree structure (no cycle)
        '''
        uf = UnionFind(2 * width * height) # Tracking if two blocks are already connected or not.
        indices = np.arange(2 * width * height)
        np.random.shuffle(indices)
        cnt, thres = 0, width * height - 1
        removed = []
        for index in indices:
            a, b = _adjacent_blocks(index) # the blocks related to this wall
            if a is None or b is None: continue # Out of bound
            if uf.merge(a, b):
                removed.append(index)
                cnt += 1
                if cnt >= thres: break # Tree feature: (N-1) connections exist
        return removed
    
    removed = frozenset(_build_spanning_tree())

    sz_width  = width  * box_size + (width  + 1) * line_width
    sz_height = height * box_size + (height + 1) * line_width 
    screen = np.zeros((sz_height, sz_width)) # Screen buffer array

    # Draw borderlines
    screen[:,:line_width] = 1 # LEFT
    screen[:line_width,:] = 1 # TOP
    screen[:,-line_width:] = 1 # RIGHT
    screen[-line_width:,:] = 1 # BOTTOM

    index = 0
    for x in range(height):
        for y in range(width):
            if index not in removed: # vertical
                x_begin = (box_size + line_width) * x
                x_end = x_begin + box_size + line_width + line_width
                y_begin = (box_size + line_width) * (y + 1)
                y_end = y_begin + line_width
                screen[x_begin:x_end,y_begin:y_end] = 1
            index += 1
            if index not in removed: # horizontal
                x_begin = (box_size + line_width) * (x + 1)
                x_end = x_begin + line_width
                y_begin = (box_size + line_width) * y
                y_end = y_begin + box_size + line_width + line_width
                screen[x_begin:x_end,y_begin:y_end] = 1
            index += 1
    
    return screen

