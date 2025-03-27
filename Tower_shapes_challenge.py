# The aim of this challenge is to find on how many ways you can build a tower having blocks with different shapes.
# Each block has two sides and it is represented by a string e.g. '+diamond, -arc'. In this solution the block rotation
# is not considered. The tower begins with the start block and ends with the end block.
# Exemplary input:
#   input = ['START,+diamond', '-diamond,-arc', '+arc,-diamond', '+diamond,END']
# and for such input there is only one way to built entire tower, thus the code should return - Output: 1

class Block:
    def __init__(self, block, parent, level, availableBlockList):
        self.block = block
        self.bottomShape = block[0]
        self.upperShape = block[1]
        self.parent = parent
        self.level = level
        self.availableBlockList = availableBlockList

def IsFitting(block1, block2):

    prefix1 = block1[1][0]
    prefix2 = block2[0][0]

    blockType1 = block1[1][1:]
    blockType2 = block2[0][1:]

    if (blockType1 == blockType2) and (prefix1 != prefix2):
        return True
    else:
        return False

def GetFittingBlocks(block1, blockList):

    fittingBlocks = []
    for i, block2 in enumerate(blockList):
        if IsFitting(block1, block2):
            fittingBlocks.append(block2)
        else:
            pass
    return fittingBlocks

def TowerCount(line):
    output = 0
    new_line = []
    for i, block in enumerate(line):
        new_line.append(block.split(','))

    start_block = new_line[0]
    end_block = new_line[-1]
    new_line.remove(start_block)
    new_line.remove(end_block)
    level = 0
    max_tower_level = len(line)-1
    BlockClassList = []

    BlockClassList.append(Block(start_block,'None', 0, new_line))

    while level <= max_tower_level:

        tempBlockClassList = BlockClassList.copy()
        for i, blockClass in enumerate(BlockClassList):
            if blockClass.level == level:
                fittingBlocks = GetFittingBlocks(blockClass.block, blockClass.availableBlockList)
                for k, newBlock in enumerate(fittingBlocks):
                    tempAvailableBlockList = blockClass.availableBlockList.copy()
                    tempAvailableBlockList.remove(newBlock)
                    tempBlockClassList.append(Block(newBlock, blockClass, level + 1, tempAvailableBlockList))
            else:
                pass
        BlockClassList = tempBlockClassList
        level +=1

    tempBlockClassList = BlockClassList.copy()

    for i, blockClass in enumerate(BlockClassList):
        if (blockClass.level == max_tower_level-1) and IsFitting(blockClass.block, end_block):
            tempBlockClassList.append(Block(end_block, blockClass, max_tower_level, []))
            output +=1



    return output



line = ['START,-diamond', '+diamond,+diamond','-diamond,-diamond','+diamond,+diamond','-diamond,END']

print('Output: ' + str(TowerCount(line)))