import mcpi.minecraft as minecraft
import mcpi.minecraftstuff as minecraftstuff
import time
import random

import utils as utils

mc = minecraft.Minecraft.create()
mcdrawing = minecraftstuff.MinecraftDrawing(mc)
def explosion(x, y, z):
    utils.draw_disc(mc,20, x, y, z, 10)
    utils.draw_disc(mc,20, x, y-1, z, 10)
    
    for a in range(10):
        utils.draw_disc(mc,4, x, y+2+a, z, 46)
    
    utils.draw_disc(mc,4, x, y+8, z, 51)     

def smoke_1(x_1, y_1, z_1, x_2, y_2, z_2):
    time.sleep(15)                       
    
    for a in range(20000):
       smoke_x = random.randint(x_1, x_2)
       smoke_y = random.randint(y_1, y_2)
       smoke_z = random.randint(z_1, z_2+a/100)
       block = random.randint(1, 100)
       if (block<51):
           block_id = 49
       elif(block<71):
           block_id = 0     
       else:
           block_id = 13
       mc.setBlock(smoke_x, smoke_y, smoke_z, block_id)
       time.sleep(0.01)
           
   
def smoke_2(x1, y1, z1, x2, y2, z2):
   smoke_x = random.randint(x1, x2)
   smoke_y = random.randint(y1, y2)
   smoke_z = random.randint(z1, z2)
   block = random.randint(1, 100)
   if (block<41):
       block_id = 49
   elif(block<81):
       block_id = 0     
   else:
       block_id = 13
   mc.setBlock(smoke_x, smoke_y, smoke_z, block_id)
   time.sleep(0.01)
   

