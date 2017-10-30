import mcpi.minecraft as minecraft
import mcpi.block as block
import mcpi.minecraftstuff as minecraftstuff
import random

mc = minecraft.Minecraft.create()
mcdrawing = minecraftstuff.MinecraftDrawing(mc)
    
#defining pillar making function
def pillar(pillar_x, pillar_y, pillar_z, pillar_type):

    if(pillar_type == "north_south"):
        x_modifier=0
        z_modifier=1
        step_1 = 2
        step_2 = 3
        step_3 = 6
        step_4 = 7

    elif(pillar_type == "east_west"):
        x_modifier=1
        z_modifier=0
        step_1 = 0
        step_2 = 1
        step_3 = 4
        step_4 = 5


    mc.setBlocks(pillar_x, pillar_y, pillar_z, pillar_x, pillar_y+7, pillar_z, 155, 2)

    mc.setBlock(pillar_x, pillar_y, pillar_z, 155, 1)
    mc.setBlock(pillar_x, pillar_y+7, pillar_z, 155, 1)

    mc.setBlock(pillar_x-x_modifier, pillar_y, pillar_z-z_modifier, 156, step_1)
    mc.setBlock(pillar_x+x_modifier, pillar_y, pillar_z+z_modifier, 156, step_2)
    mc.setBlock(pillar_x-x_modifier, pillar_y+7, pillar_z-z_modifier, 156, step_3)
    mc.setBlock(pillar_x+x_modifier, pillar_y+7, pillar_z+z_modifier, 156, step_4)

#defining corner pillar making function
def corner_pillar(pillar_x, pillar_y, pillar_z, pillar_type):

    if(pillar_type == "south_east"):
        x_modifier=1
        z_modifier=1
        step_1 = 1
        step_2 = 3
        step_3 = 5
        step_4 = 7
    elif(pillar_type == "south_west"):
        x_modifier=-1
        z_modifier=1
        step_1 = 0
        step_2 = 3
        step_3 = 4
        step_4 = 7
    elif(pillar_type == "north_east"):
        x_modifier=1
        z_modifier=-1
        step_1 = 1
        step_2 = 2
        step_3 = 5
        step_4 = 6
    elif(pillar_type == "north_west"):
        x_modifier=-1
        z_modifier=-1
        step_1 = 0
        step_2 = 2
        step_3 = 4
        step_4 = 6
        
    


    mc.setBlocks(pillar_x, pillar_y, pillar_z, pillar_x, pillar_y+7, pillar_z, 155, 2)

    mc.setBlock(pillar_x, pillar_y, pillar_z, 155, 1)
    mc.setBlock(pillar_x, pillar_y+7, pillar_z, 155, 1)

    mc.setBlock(pillar_x+x_modifier, pillar_y, pillar_z, 156, step_1)
    mc.setBlock(pillar_x, pillar_y, pillar_z+z_modifier, 156, step_2)
    mc.setBlock(pillar_x+x_modifier, pillar_y+7, pillar_z, 156, step_3)
    mc.setBlock(pillar_x, pillar_y+7, pillar_z+z_modifier, 156, step_4)        
    
def create_forum(x,y,z):
    forum_x = x
    forum_y = y
    forum_z = z
    
    #forums bottom right co-ordinates
    #forum_x = 0
    #forum_y = -1
    #forum_z = 0
    
    #base pillar co-ordinates
    pillar_x = forum_x
    pillar_y = forum_y+1
    pillar_z = forum_z
    
    #create forum
    mc.setBlocks(forum_x, forum_y+15, forum_z-10, forum_x+37, forum_y+1, forum_z-156, block.AIR.id)
    
    mc.setBlocks(forum_x, forum_y, forum_z, forum_x+37, forum_y, forum_z-156, 159, 14)
    
    #add pillars
    for a in range(1, 51):
        pillar(pillar_x+37, pillar_y, pillar_z-(a*3),"north_south")
    
    for a in range(1, 48):
        pillar(pillar_x, pillar_y, pillar_z-(a*3), "north_south")
    
    for a in range(1, 6):
       pillar(pillar_x+(a*3), pillar_y, pillar_z, "east_west")
    
    for a in range(5):
      pillar(pillar_x+22+(a*3), pillar_y, pillar_z, "east_west")
    
    corner_pillar(pillar_x, pillar_y, pillar_z, "north_east")
    corner_pillar(pillar_x+37, pillar_y, pillar_z, "north_west")
    
    #make temple of jupiter
    mc.setBlocks(forum_x+26, 0, forum_z-156, forum_x+10, 2, forum_z-120, 159, 10)
    
    mc.setBlocks(forum_x+11, 0, forum_z-120, forum_x+10, 0, forum_z-120, 156, 3)
    mc.setBlocks(forum_x+11, 1, forum_z-120, forum_x+10, 2, forum_z-120, 0)
    mc.setBlocks(forum_x+11, 1, forum_z-121, forum_x+10, 1, forum_z-121, 156, 3)
    mc.setBlocks(forum_x+11, 2, forum_z-120, forum_x+10, 2, forum_z-121, 0)
    mc.setBlocks(forum_x+11, 2, forum_z-122, forum_x+10, 2, forum_z-122, 156, 3)
    
    mc.setBlocks(forum_x+26, 0, forum_z-120, forum_x+25, 0, forum_z-120, 156, 3)
    mc.setBlocks(forum_x+26, 1, forum_z-120, forum_x+25, 2, forum_z-120, 0)
    mc.setBlocks(forum_x+26, 1, forum_z-121, forum_x+25, 1, forum_z-121, 156, 3)
    mc.setBlocks(forum_x+26, 2, forum_z-120, forum_x+25, 2, forum_z-121, 0)
    mc.setBlocks(forum_x+26, 2, forum_z-122, forum_x+25, 2, forum_z-122, 156, 3)
    
    #make altar
    mc.setBlocks(forum_x+17, 3, forum_z-120, forum_x+19, 3, forum_z-120, 24, 2)
    
    #add columns
    pillar_x = 10
    pillar_y = 3
    pillar_z = -126
    
    for a in range(1, 4):
        pillar(pillar_x, pillar_y, pillar_z-(a*3),"north_south")
    
    for a in range(1, 4):
        pillar(pillar_x+16, pillar_y, pillar_z-(a*3), "north_south")
    
    for a in range(1, 3):
       pillar(pillar_x+(a*3), pillar_y, pillar_z, "east_west")
    
    for a in range(2):
      pillar(pillar_x+10+(a*3), pillar_y, pillar_z, "east_west")
    
    corner_pillar(pillar_x, pillar_y, pillar_z, "north_east")
    corner_pillar(pillar_x+16, pillar_y, pillar_z, "north_west")
    
    #build front wall
    mc.setBlocks(forum_x+10,3,forum_z-137,forum_x+26,10,forum_z-137,24)
    mc.setBlocks(forum_x+17,3,forum_z-137,forum_x+20,8,forum_z-137,0)
    
    #build side walls
    mc.setBlocks(forum_x+10,3,forum_z-138,forum_x+10,10,forum_z-156,24)
    mc.setBlocks(forum_x+26,3,forum_z-138,forum_x+26,10,forum_z-156,24)
    
    #build back wall
    mc.setBlocks(forum_x+10,3,forum_z-156,forum_x+26,10,forum_z-156,24)
    
    #build roof
    #front of roof
    
    points = []
    points.append(minecraft.Vec3(forum_x+26,11,forum_z-126))
    points.append(minecraft.Vec3(forum_x+18,15,forum_z-126))
    points.append(minecraft.Vec3(forum_x+10,11,forum_z-126))
    
    mcdrawing.drawFace(points, True, 24, 1) 
    
    #back roof
    
    points = []
    points.append(minecraft.Vec3(forum_x+26,11,forum_z-156))
    points.append(minecraft.Vec3(forum_x+18,15,forum_z-156))
    points.append(minecraft.Vec3(forum_x+10,11,forum_z-156))
    
    mcdrawing.drawFace(points, True, 24, 1) 
       
    #middle roof
    points = []
    points.append(minecraft.Vec3(forum_x+26,11,forum_z-137))
    points.append(minecraft.Vec3(forum_x+18,15,forum_z-137))
    points.append(minecraft.Vec3(forum_x+10,11,forum_z-137))
    
    mcdrawing.drawFace(points, True, 24, 1)
    
    #Fill in portico with beams
    for a in range(10):
        points = []
        points.append(minecraft.Vec3(forum_x+26,11,forum_z-127-a))
        points.append(minecraft.Vec3(forum_x+18,15,forum_z-127-a))
        points.append(minecraft.Vec3(forum_x+10,11,forum_z-127-a))
        mcdrawing.drawFace(points, False, 24, 1)
        if(a % 2 == 0):
            mc.setBlocks(forum_x+24,11,forum_z-127-a,forum_x+12,11,forum_z-127-a,0)
        
    #Fill in roof with beams
    for a in range(18):
        points = []
        points.append(minecraft.Vec3(forum_x+26,11,forum_z-138-a))
        points.append(minecraft.Vec3(forum_x+18,15,forum_z-138-a))
        points.append(minecraft.Vec3(forum_x+10,11,forum_z-138-a))
        mcdrawing.drawFace(points, False, 24, 1)
        if(a % 2 == 0):
            mc.setBlocks(forum_x+24,11,forum_z-138-a,12,11,forum_z-138-a,0)
            
    #add light
    mc.setBlocks(forum_x+25,10, forum_z-138, forum_x+25, 10, forum_z-155, 89)
    mc.setBlocks(forum_x+11,10, forum_z-138, forum_x+11, 10, forum_z-155, 89)
    mc.setBlocks(forum_x+12,10, forum_z-155, forum_x+24, 10, forum_z-155, 89)
    
    #add cella
    cella_x = forum_x+11
    cella_y = 3
    cella_z = forum_z-148
    
    for a in range(4):
        mc.setBlocks(cella_x, cella_y, cella_z, cella_x+2,cella_y+2,cella_z-2,49)
        mc.setBlocks(cella_x+1, cella_y, cella_z-3, cella_x+1,cella_y+2,cella_z-7,49)
        mc.setBlock(cella_x+1, cella_y+3, cella_z-1, 138)
        mc.setBlocks(cella_x, cella_y, cella_z+2, cella_x+2,cella_y,cella_z+5, 171, (random.randint(0, 15)))
        cella_x += 4
