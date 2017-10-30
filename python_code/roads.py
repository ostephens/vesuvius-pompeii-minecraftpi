import mcpi.minecraft as minecraft
import mcpi.minecraftstuff as minecraftstuff

mc = minecraft.Minecraft.create()
mcdrawing = minecraftstuff.MinecraftDrawing(mc)

road_x = 0
road_z = 0

def road(x,z,length,direction,width):
    if(direction=="s"):
        mc.setBlocks(x-1,0,z,x-1,-1,z+length,44)
        mc.setBlocks(x+width+1,0,z,x+width+1,-1,z+length,44)
        mc.setBlocks(x,-1,z,x+width,-1,z+length,44,5)
        mc.setBlocks(x,0,z-1,x+width,0,z+length+1,0)
    elif(direction=="n"):
        mc.setBlocks(x-1,0,z,x-1,-1,z-length,44)
        mc.setBlocks(x+width+1,0,z,x+width+1,-1,z-length,44)
        mc.setBlocks(x,-1,z,x+width,-1,z-length,44,5)
        mc.setBlocks(x,0,z+1,x+width,0,z-length-1,0)
    elif(direction=="e"):
        mc.setBlocks(x,0,z-1,x+length,-1,z-1,44)
        mc.setBlocks(x,0,z+width+1,x+length,-1,z+width+1,44)
        mc.setBlocks(x,-1,z,x+length,-1,z+width,44,5)
        mc.setBlocks(x-1,0,z,x+length-1,0,z+width,0)
    elif(direction=="w"):
        mc.setBlocks(x,0,z-1,x-length,-1,z-1,44)
        mc.setBlocks(x,0,z+width+1,x-length,-1,z+width+1,44)
        mc.setBlocks(x,-1,z,x-length,-1,z+width,44,5)        
        mc.setBlocks(x-1,0,z,x-length-1,0,z+width,0)
        
def house(x,z,direction):
    y_mod = 6
    if(direction=="n"):
        x_mod = -18
        z_mod = 28
    elif(direction=="s"):
        x_mod = 18
        z_mod = -28
    elif(direction=="e"):
        x_mod = -28
        z_mod = -18
    elif(direction=="w"):
        x_mod = 28
        z_mod = 18
        
    z_mid = z+(z_mod//2)
    x_mid = x+(x_mod//2)

    mc.setBlocks(x,0,z,x,6,z+z_mod,24)
    mc.setBlocks(x,0,z,x+x_mod,6,z,24)
    mc.setBlocks(x+x_mod,0,z,x+x_mod,6,z+z_mod,24)
    mc.setBlocks(x,0,z+z_mod,x+x_mod,6,z+z_mod,24)
    
    #build roof
    #roof panel 1
    points = []
    points.append(minecraft.Vec3(x,6,z))
    points.append(minecraft.Vec3(x_mid,12,z_mid))
    points.append(minecraft.Vec3(x+x_mod,6,z))
    mcdrawing.drawFace(points, True, 43,4) 
    
    #roof panel 2
    points = []
    points.append(minecraft.Vec3(x,6,z))
    points.append(minecraft.Vec3(x_mid,12,z_mid))
    points.append(minecraft.Vec3(x,6,z+z_mod))
    mcdrawing.drawFace(points, True, 43,4)
       
    #roof panel 3
    points = []
    points.append(minecraft.Vec3(x+x_mod,6,z))
    points.append(minecraft.Vec3(x_mid,12,z_mid))
    points.append(minecraft.Vec3(x+x_mod,6,z+z_mod))    
    mcdrawing.drawFace(points, True, 43,4)
    
    #roof panel 4
    points = []
    points.append(minecraft.Vec3(x+x_mod,6,z+z_mod))
    points.append(minecraft.Vec3(x_mid,12,z_mid))
    points.append(minecraft.Vec3(x,6,z+z_mod))
    mcdrawing.drawFace(points, True, 43,4)
    
    #door
    if(direction=="n" or direction=="s"):
        mc.setBlocks(x_mid,0,z,x_mid,2,z,0)
    if(direction=="e" or direction=="w"):
        mc.setBlocks(x,0,z_mid,x,2,z_mid,0)
    
    #windows?
    
    #clear infront of door
    
    
def create_city(x,z):
    road_x = x
    road_z = z
    #Via Marina
    road(road_x+38,road_z-24,150,"e",3)
    for a in range(5):
        house(road_x+40+30*a,road_z-26,"s")
        house(road_x+66+30*a,road_z-19,"n")
    #Via dell'Abbondanza
    road(road_x-1,road_z-24,150,"w",3)
    for a in range(5):
        house(road_x-31-30*a,road_z-26,"s")
        house(road_x-5-30*a,road_z-19,"n")
    
    #Via del Soprastanti
    road(road_x+0,road_z-161,150,"e",3)
    for a in range(5):
        house(road_x+40+30*a,road_z-163,"s")
        house(road_x+66+30*a,road_z-156,"n")
    #Via delgi Augustali
    road(road_x-1,road_z-161,150,"w",3)
    for a in range(5):
        house(road_x-31-30*a,road_z-163,"s")
        house(road_x-5-30*a,road_z-156,"n")
    
    #Via delle Terme
    road(road_x+0,road_z-242,150,"e",3)
    for a in range(5):
        house(road_x+45+30*a,road_z-244,"s")
        house(road_x+66+30*a,road_z-237,"n")
    #Via della Fortuna
    road(road_x-1,road_z-242,150,"w",3)
    for a in range(5):
        house(road_x-31-30*a,road_z-244,"s")
        house(road_x-5-30*a,road_z-237,"n")
    
    
    #Via del Foro
    road(road_x+35,road_z-162,75,"n",3)
    #Vicolo delle Terme
    road(road_x-3,road_z-162,75,"n",1)
    #Vicolo delle Fullonica
    road(road_x-3,road_z-244,75,"n",1)
    #To villa back door
    road(road_x+0,road_z-272,41,"e",1)
