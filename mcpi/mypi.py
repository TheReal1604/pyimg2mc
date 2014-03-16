#!/usr/bin/python
__author__ = 'Brian'

import mcpi.minecraft as minecraft
import mcpi.block as block
servername = "46.38.238.188"

world = minecraft.Minecraft.create(address="fastreboot.de", port=4711)

[x,y,z] = world.player.getPos()

# msg= "%s" % x,y,z
# print msg
# world.postToChat(msg)

#for i in range(10):
#    world.setBlock( x, y+i, z+10+i, block.GLOWSTONE_BLOCK )
#    world.setBlock( x, y+10-i, z+20+i, block.GLOWSTONE_BLOCK )

def cuboid(x,y,z,width,depth,material):
    world.setBlocks(x-width, y, z-width, x+width, y+depth, z+width, material)
    world.setBlocks()

def room(x,y,z,width,depth,material):
#    create solid cuboid
    cuboid(x,y,z,width,depth,material)
# fill with air
    cuboid(x,y+1,z,width-1,depth-2,block.AIR)

room(x,y-1,z,5,4,block.DIAMOND_BLOCK)