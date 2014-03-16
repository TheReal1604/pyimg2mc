#!/usr/bin/python
__author__ = 'Brian'

import mcpi.minecraft as minecraft
import mcpi.block as block
import Image

SECUREDISTANCE=10

im = Image.open('cat.png')
width, height = im.size
rgb_im = im.convert('RGB')


pic = []

for x in range(width):
    row = []
    for y in range(height):
        r,g,b = rgb_im.getpixel((x, y))
        p = r << 15 | g << 8 | b
        row.append(p);
    pic.append(row)

servername = "46.38.238.188"

world = minecraft.Minecraft.create(address="fastreboot.de", port=4711)
[x,y,z] = world.player.getPos()

# msg= "%s" % x,y,z
# print msg
# world.postToChat(msg)


for ix in range(width):
    for iy in range(height):
        if pic[ix][iy] > 1036335 and pic[ix][iy] <= 2*1036335:
            world.setBlock( x+ix, y+height-iy, z+SECUREDISTANCE, block.WOOL.id, 1)
        elif pic[ix][iy] > 2*1036335 and pic[ix][iy] <= 3*1036335:
            world.setBlock( x+ix, y+height-iy, z+SECUREDISTANCE, block.WOOL.id, 8)
        elif pic[ix][iy] > 3*1036335 and pic[ix][iy] <= 4*1036335:
            world.setBlock( x+ix, y+height-iy, z+SECUREDISTANCE, block.WOOL.id, 14)
        elif pic[ix][iy] > 4*1036335 and pic[ix][iy] <= 5*1036335:
            world.setBlock( x+ix, y+height-iy, z+SECUREDISTANCE, block.WOOL.id, 11)
        elif pic[ix][iy] > 5*1036335 and pic[ix][iy] <= 6*1036335:
            world.setBlock( x+ix, y+height-iy, z+SECUREDISTANCE, block.WOOL.id, 14)
        elif pic[ix][iy] > 6*1036335 and pic[ix][iy] <= 7*1036335:
            world.setBlock( x+ix, y+height-iy, z+SECUREDISTANCE, block.WOOL.id, 10)
        elif pic[ix][iy] > 7*1036335 and pic[ix][iy] <= 8*1036335:
            world.setBlock( x+ix, y+height-iy, z+SECUREDISTANCE, block.WOOL.id, 13)
        elif pic[ix][iy] > 8*1036335 and pic[ix][iy] <= 9*1036335:
            world.setBlock( x+ix, y+height-iy, z+SECUREDISTANCE, block.WOOL.id, 7)
        elif pic[ix][iy] > 9*1036335 and pic[ix][iy] <= 10*1036335:
            world.setBlock( x+ix, y+height-iy, z+SECUREDISTANCE, block.WOOL.id, 6)
        elif pic[ix][iy] > 10*1036335 and pic[ix][iy] <= 11*1036335:
            world.setBlock( x+ix, y+height-iy, z+SECUREDISTANCE, block.WOOL.id, 2)
        elif pic[ix][iy] > 11*1036335 and pic[ix][iy] <= 12*1036335:
            world.setBlock( x+ix, y+height-iy, z+SECUREDISTANCE, block.WOOL.id, 12)
        elif pic[ix][iy] > 12*1036335 and pic[ix][iy] <= 13*1036335:
            world.setBlock( x+ix, y+height-iy, z+SECUREDISTANCE, block.WOOL.id, 8)
        elif pic[ix][iy] > 13*1036335 and pic[ix][iy] <= 14*1036335:
            world.setBlock( x+ix, y+height-iy, z+SECUREDISTANCE, block.WOOL.id, 7)
        elif pic[ix][iy] > 14*1036335 and pic[ix][iy] <= 15*1036335:
            world.setBlock( x+ix, y+height-iy, z+SECUREDISTANCE, block.WOOL.id, 12)
        else:
            world.setBlock( x+ix, y+height-iy, z+SECUREDISTANCE, block.WOOL.id, 15)


#def cuboid(x,y,z,width,depth,material):
#    world.setBlocks(x-width, y, z-width, x+width, y+depth, z+width, material)
#    world.setBlocks()
#
#def room(x,y,z,width,depth,material):
##    create solid cuboid
#    cuboid(x,y,z,width,depth,material)
## fill with air
#    cuboid(x,y+1,z,width-1,depth-2,block.AIR)
#
#room(x,y-1,z,5,4,block.DIAMOND_BLOCK)
