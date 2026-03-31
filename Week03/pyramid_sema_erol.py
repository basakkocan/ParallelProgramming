def calculate_pyramid_height(number_of_blocks):
    height = 0
    blocks_used = 0
    level = 1
    
    while blocks_used + level <= number_of_blocks:
        blocks_used += level
        height += 1
        level += 1
    
    return height
