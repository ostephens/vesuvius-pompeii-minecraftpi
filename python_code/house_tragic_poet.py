import mcpi.minecraft as minecraft
import random
import mcpi.minecraftstuff as minecraftstuff

mc = minecraft.Minecraft.create()
mcdrawing = minecraftstuff.MinecraftDrawing(mc)

def create_htp(x,y,z):
    #house_x = 0
    #house_y = 0
    #house_z = -269
    house_x = x
    house_y = y
    house_z = z
    
    
    #Clear space
    mc.setBlocks(house_x, house_y, house_z, house_x+42, house_y+50, house_z+25, 0)
    
    #Make floor
    #mc.setBlocks(house_x, house_y, house_z, house_x+42, house_y, house_z+19, 43, 7)
    
    #Make walls
    mc.setBlocks(house_x+41,house_y+0,house_z+0,house_x+41,house_y+6,house_z+25,24)
    mc.setBlocks(house_x+38,house_y+0,house_z+0,house_x+38,house_y+6,house_z+4,98,2)
    mc.setBlocks(house_x+34,house_y+0,house_z+0,house_x+34,house_y+6,house_z+4,98,2)
    mc.setBlocks(house_x+32,house_y+0,house_z+16,house_x+32,house_y+6,house_z+25,98,2)
    mc.setBlocks(house_x+30,house_y+0,house_z+18,house_x+30,house_y+6,house_z+20,98,2)
    mc.setBlocks(house_x+28,house_y+0,house_z+0,house_x+28,house_y+6,house_z+11,98,2)
    mc.setBlocks(house_x+28,house_y+0,house_z+14,house_x+28,house_y+6,house_z+17,98,2)
    mc.setBlocks(house_x+28,house_y+0,house_z+18,house_x+28,house_y+6,house_z+25,24)
    mc.setBlocks(house_x+23,house_y+0,house_z+0,house_x+23,house_y+6,house_z+4,98,2)
    mc.setBlocks(house_x+21,house_y+0,house_z+4,house_x+21,house_y+6,house_z+11,98,2)
    mc.setBlocks(house_x+21,house_y+0,house_z+14,house_x+21,house_y+6,house_z+18,98,2)
    mc.setBlocks(house_x+18,house_y+0,house_z+0,house_x+18,house_y+6,house_z+5,98,2)
    mc.setBlocks(house_x+18,house_y+0,house_z+14,house_x+18,house_y+6,house_z+18,98,2)
    mc.setBlocks(house_x+13,house_y+0,house_z+0,house_x+13,house_y+6,house_z+5,98,2)
    mc.setBlocks(house_x+12,house_y+0,house_z+14,house_x+12,house_y+6,house_z+18,98,2)
    mc.setBlocks(house_x+9,house_y+0,house_z+0,house_x+9,house_y+6,house_z+7,98,2)
    mc.setBlocks(house_x+9,house_y+0,house_z+11,house_x+9,house_y+6,house_z+18,98,2)
    mc.setBlocks(house_x+0,house_y+0,house_z+0,house_x+0,house_y+6,house_z+18,24)
    mc.setBlocks(house_x+0,house_y-1,house_z+0,house_x+41,house_y+6,house_z+0,24)
    mc.setBlocks(house_x+9,house_y+0,house_z+5,house_x+21,house_y+6,house_z+5,98,2)
    mc.setBlocks(house_x+21,house_y+0,house_z+4,house_x+38,house_y+6,house_z+4,98,2)
    mc.setBlocks(house_x+0,house_y+0,house_z+7,house_x+9,house_y+6,house_z+7,98,2)
    mc.setBlocks(house_x+0,house_y+0,house_z+11,house_x+9,house_y+6,house_z+11,98,2)
    mc.setBlocks(house_x+21,house_y+0,house_z+11,house_x+28,house_y+6,house_z+11,98,2)
    mc.setBlocks(house_x+12,house_y+0,house_z+14,house_x+18,house_y+6,house_z+14,98,2)
    mc.setBlocks(house_x+21,house_y+0,house_z+14,house_x+28,house_y+6,house_z+14,98,2)
    mc.setBlocks(house_x+29,house_y+0,house_z+18,house_x+30,house_y+6,house_z+18,98,2)
    mc.setBlocks(house_x+0,house_y+0,house_z+18,house_x+28,house_y+6,house_z+18,24)
    mc.setBlocks(house_x+32,house_y+0,house_z+16,house_x+41,house_y+6,house_z+16,98,2)
    mc.setBlocks(house_x+28,house_y+0,house_z+25,house_x+41,house_y+6,house_z+25,24)
    
    #Make Doors
    mc.setBlocks(house_x+0,house_y+0,house_z+2,house_x+0,house_y+3,house_z+4,0)
    mc.setBlocks(house_x+0,house_y+0,house_z+9,house_x+0,house_y+2,house_z+9,0)
    mc.setBlocks(house_x+0,house_y+0,house_z+14,house_x+0,house_y+3,house_z+16,0)
    mc.setBlocks(house_x+2,house_y+0,house_z+7,house_x+2,house_y+2,house_z+7,0)
    mc.setBlocks(house_x+2,house_y+0,house_z+11,house_x+2,house_y+2,house_z+11,0)
    mc.setBlocks(house_x+12,house_y+0,house_z+5,house_x+12,house_y+2,house_z+5,0)
    mc.setBlocks(house_x+16,house_y+0,house_z+5,house_x+16,house_y+2,house_z+5,0)
    mc.setBlocks(house_x+15,house_y+0,house_z+14,house_x+16,house_y+2,house_z+14,0)
    mc.setBlocks(house_x+19,house_y+0,house_z+5,house_x+19,house_y+2,house_z+5,0)
    mc.setBlocks(house_x+21,house_y+0,house_z+6,house_x+21,house_y+4,house_z+9,0)
    mc.setBlocks(house_x+25,house_y+0,house_z+4,house_x+26,house_y+3,house_z+4,0)
    mc.setBlocks(house_x+28,house_y+0,house_z+6,house_x+28,house_y+4,house_z+9,0)
    mc.setBlocks(house_x+28,house_y+0,house_z+16,house_x+28,house_y+2,house_z+16,0)
    mc.setBlocks(house_x+31,house_y+0,house_z+4,house_x+32,house_y+2,house_z+4,0)
    mc.setBlocks(house_x+36,house_y+0,house_z+4,house_x+36,house_y+2,house_z+4,0)
    mc.setBlocks(house_x+39,house_y+0,house_z+0,house_x+40,house_y+2,house_z+0,0)
    mc.setBlocks(house_x+36,house_y+0,house_z+16,house_x+38,house_y+3,house_z+16,0)
    
    
    #make floor
    mc.setBlocks(house_x, house_y-1, house_z, house_x+28, house_y-1, house_z+18, 43, 3)
    mc.setBlocks(house_x+29, house_y-1, house_z+1, house_x+37, house_y-1, house_z+3, 43, 3)
    mc.setBlocks(house_x+33, house_y-1, house_z+17, house_x+40, house_y-1, house_z+24, 159, 11)
    
    #Make pool in atrium
    mc.setBlocks(house_x+13, house_y-1, house_z+8, house_x+16, house_y-1, house_z+10, 8)
    
    #make step up
    mc.setBlocks(house_x+22, house_y+0, house_z+5, house_x+27, house_y+0, house_z+10, 44, 4)
    
    #make counters
    mc.setBlocks(house_x+1, house_y, house_z+1, house_x+1, house_y, house_z+6, 5, 4)
    mc.setBlocks(house_x+1, house_y, house_z+12, house_x+1, house_y, house_z+17, 5, 4)
    
    #add beds
    mc.setBlock(house_x+12,house_y+0,house_z+2,26)
    mc.setBlock(house_x+12,house_y+0,house_z+3,26,8)
    
    mc.setBlock(house_x+15,house_y+0,house_z+1,26,3)
    mc.setBlock(house_x+16,house_y+0,house_z+1,26,11)
    
    mc.setBlock(house_x+20,house_y+0,house_z+1,26,3)
    mc.setBlock(house_x+21,house_y+0,house_z+1,26,11)
    
    mc.setBlock(house_x+25,house_y+0,house_z+1,26,3)
    mc.setBlock(house_x+26,house_y+0,house_z+1,26,11)
    
    mc.setBlock(house_x+36,house_y+0,house_z+1,26,3)
    mc.setBlock(house_x+37,house_y+0,house_z+1,26,11)
    
    mc.setBlock(house_x+31,house_y+0,house_z+1,26,3)
    mc.setBlock(house_x+32,house_y+0,house_z+1,26,11)
    
    #add book shelves
    mc.setBlocks(house_x+22, house_y, house_z+15, house_x+27, house_y+2, house_z+15, 47)
    mc.setBlocks(house_x+22, house_y, house_z+17, house_x+27, house_y+2, house_z+17, 47)
    mc.setBlocks(house_x+22, house_y, house_z+10, house_x+27, house_y+2, house_z+10, 47)
    mc.setBlocks(house_x+14, house_y, house_z+16, house_x+14, house_y+2, house_z+17, 47)
    mc.setBlocks(house_x+16, house_y, house_z+16, house_x+16, house_y+2, house_z+17, 47)
    
    #make garden
    mc.setBlocks(house_x+31, house_y, house_z+7, house_x+31, house_y, house_z+9, 18)
    mc.setBlocks(house_x+31, house_y, house_z+11, house_x+31, house_y, house_z+13, 18)
    mc.setBlocks(house_x+38, house_y, house_z+7, house_x+38, house_y, house_z+9, 18)
    mc.setBlocks(house_x+38, house_y, house_z+11, house_x+38, house_y, house_z+13, 18)
    
    mc.setBlocks(house_x+32, house_y, house_z+7, house_x+33, house_y, house_z+7, 18)
    mc.setBlocks(house_x+36, house_y, house_z+7, house_x+37, house_y, house_z+7, 18)
    mc.setBlocks(house_x+32, house_y, house_z+13, house_x+33, house_y, house_z+13, 18)
    mc.setBlocks(house_x+36, house_y, house_z+13, house_x+37, house_y, house_z+13, 18)
    
    mc.setBlocks(house_x+34, house_y-1, house_z+10, house_x+35, house_y-1, house_z+10, 8)
    mc.setBlocks(house_x+34, house_y, house_z+10, house_x+35, house_y, house_z+10, 111)
    
    mc.setBlock(house_x+36,house_y,house_z+9, 38, (random.randint(0, 8)))
    mc.setBlock(house_x+33,house_y,house_z+9, 38, (random.randint(0, 8)))
    mc.setBlock(house_x+34,house_y,house_z+9, 38, (random.randint(0, 8)))
    mc.setBlock(house_x+35,house_y,house_z+9, 38, (random.randint(0, 8)))
    mc.setBlock(house_x+36,house_y,house_z+11, 38, (random.randint(0, 8)))
    mc.setBlock(house_x+34,house_y,house_z+11, 38, (random.randint(0, 8)))
    mc.setBlock(house_x+33,house_y,house_z+11, 38, (random.randint(0, 8)))
    mc.setBlock(house_x+35,house_y,house_z+11, 38, (random.randint(0, 8)))
    mc.setBlock(house_x+33,house_y,house_z+10, 38, (random.randint(0, 8)))
    mc.setBlock(house_x+36,house_y,house_z+10, 38, (random.randint(0, 8)))
    
    #make lavatory
    mc.setBlocks(house_x+29, house_y-1, house_z+24, house_x+29, house_y-1, house_z+19, 8)
    mc.setBlock(house_x+29, house_y, house_z+24, 96)
    mc.setBlock(house_x+29, house_y, house_z+23, 43, 3)
    mc.setBlock(house_x+29, house_y, house_z+22, 96, 1)
    mc.setBlock(house_x+29, house_y, house_z+21, 43, 3)
    mc.setBlock(house_x+29, house_y, house_z+20, 96)
    mc.setBlock(house_x+29, house_y, house_z+19, 43, 3)
    mc.setBlock(house_x+29, house_y+1, house_z+19, 19)
    mc.setBlock(house_x+29, house_y+1, house_z+21, 19)
    mc.setBlock(house_x+29, house_y+1, house_z+23, 19)
    
    #make roof
    for a in range(29):
        for b in range(5):
            mc.setBlock(house_x+a,house_y+7+b,house_z-1+b*2,109,2)
            mc.setBlock(house_x+a,house_y+7+b,house_z+b*2,45)
            mc.setBlock(house_x+a,house_y+7+b,house_z+19-b*2,109,3)
            mc.setBlock(house_x+a,house_y+7+b,house_z+18-b*2,45)
            if(a==0 or a==28):
                for c in range(1+b*2,18-b*2):
                    if(c % 2 == 1):
                        mc.setBlock(house_x+a,house_y+7+b,house_z+c,43,5) #stone brick
                    else:
                        mc.setBlock(house_x+a,house_y+7+b,house_z+c,43,4) #brick
        mc.setBlock(house_x+a,house_y+12,house_z+9,155)
        mc.setBlock(house_x+a,house_y+13,house_z+9,44,7)
        mc.setBlock(house_x+a,house_y+12,house_z+8,156,2)
        mc.setBlock(house_x+a,house_y+12,house_z+10,156,3)
    
    mc.setBlocks(house_x+13,house_y+2,house_z+8,house_x+16,house_y+15,house_z+10,0)
    mc.setBlocks(house_x+29, house_y+6, house_z+0, house_x+38, house_y+6, house_z+4, 43,4)
    
    for a in range(8):
        if (a % 2 == 0):
            b_start = 0
        else:
            b_start = 1
        for b in range(b_start ,8):
            if((b-b_start) % 2 == 0):
                mc.setBlock(house_x+33+a,house_y+6,house_z+17+b, 43, 4)
    
    #make windows
    mc.setBlocks(house_x+11,house_y+1,house_z+0,house_x+11,house_y+2,house_z+0,102)
    mc.setBlocks(house_x+15,house_y+1,house_z+0,house_x+16,house_y+2,house_z+0,102)
    mc.setBlocks(house_x+14,house_y+3,house_z+18,house_x+14,house_y+4,house_z+18,102)
    mc.setBlocks(house_x+16,house_y+3,house_z+18,house_x+16,house_y+4,house_z+18,102)
    mc.setBlocks(house_x+25,house_y+1,house_z+0,house_x+26,house_y+2,house_z+0,102)
    mc.setBlocks(house_x+3,house_y+3,house_z+0,house_x+6,house_y+1,house_z+0,102)
    mc.setBlocks(house_x+3,house_y+3,house_z+18,house_x+6,house_y+1,house_z+18,102)
    mc.setBlocks(house_x+21,house_y+1,house_z+0,house_x+19,house_y+2,house_z+0,102)
    mc.setBlocks(house_x+23,house_y+3,house_z+18,house_x+23,house_y+4,house_z+18,102)
    mc.setBlocks(house_x+26,house_y+3,house_z+18,house_x+26,house_y+4,house_z+18,102)
    mc.setBlocks(house_x+26,house_y+1,house_z+0,house_x+25,house_y+2,house_z+0,102)
    mc.setBlocks(house_x+31,house_y+1,house_z+0,house_x+32,house_y+2,house_z+0,102)
    mc.setBlocks(house_x+36,house_y+1,house_z+0,house_x+37,house_y+2,house_z+0,102)
    mc.setBlocks(house_x+19,house_y+1,house_z+18,house_x+20,house_y+2,house_z+18,102)
    
    #clear front and side
    mc.setBlocks(house_x-1,house_y,house_z-1,house_x-1,house_y,house_z+18,0)
    mc.setBlocks(house_x-1,house_y-1,house_z,house_x-1,house_y-1,house_z+18,109,0)
    mc.setBlocks(house_x,house_y,house_z-1,house_x+41,house_y,house_z-1,0)