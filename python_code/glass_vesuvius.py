import mcpi.minecraft as minecraft
import mcpi.minecraftstuff as minecraftstuff
import time
import math
import random

mc = minecraft.Minecraft.create()
mcdrawing = minecraftstuff.MinecraftDrawing(mc)

#player starting co-ordinates
home_x = 19
home_y = 200
home_z = -419

v_x = 19
v_y = 0
v_z = -419

def draw_disc(radius,cx,cy,cz,block):
    for i in range(radius*2-1):
        for a in range(radius*2-1):
            side_1 = radius-a
            side_2 = radius-i
            hypotenuse = math.sqrt(side_1**2+side_2**2)
            if (hypotenuse<radius):
                mc.setBlocks(cx-side_1,cy,cz-side_2,cx+side_1,cy,cz-side_2,block)
                break
                    
def draw_ring(radius, width,cx,cy,cz,block):
    for i in range(radius*2-1):
        for a in range(radius*2-1):
            side_1 = radius-a
            side_2 = radius-i
            hypotenuse = math.sqrt(side_1**2+side_2**2)
            if (hypotenuse<radius and hypotenuse > radius - width):
                if(mc.getBlock(cx-side_1,cy,cz-side_2) != block):
                    mc.setBlock(cx-side_1,cy,cz-side_2, block)

#mc.setBlocks(10, 0, 10, 20, 10, 20, 46, 1)
#time.sleep(5)
#mc.setBlock(15, 11, 15, 51)
mc.player.setPos(home_x, home_y, home_z)


#mc.setBlocks(0,0,0,120,0,120,1)
r=100
for a in range(30):
    draw_disc(r, v_x, v_y+a, v_z, 20)
    r = r - random.randint(2,3)
    
for a in range(30,50):
    draw_disc(r, v_x, v_y+a, v_z, 20)
    r = r - random.randint(0,2)
    
