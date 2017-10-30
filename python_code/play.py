import mcpi.minecraft as minecraft
import time

import utils as utils
import forum as forum
import roads as roads
import vesuvius_small as vesuvius
import house_tragic_poet as htp
import explosion as explosion

mc = minecraft.Minecraft.create()

house_x = 0
house_y = 0
house_z = -269

roads.create_city(0,0)
time.sleep(10)
vesuvius.create_vesuvius(19,0,-355)
htp.create_htp(house_x, house_y, house_z)
forum.create_forum(0,-1,0)
messages = utils.read_info("info.txt")


#player starting co-ordinates
home_x = 19
home_y = 0
home_z = -21

mc.player.setPos(home_x, home_y, home_z)

    


while True:
    pos = mc.player.getTilePos()
    if pos.x<21 and pos.x>16 and pos.z == -21:
        utils.post_messages(mc,messages,"Forum",3)
    elif (pos.x < 24 and pos.x>12 and pos.z > -119 and pos.z < -114):
        utils.post_messages(mc,messages,"Jupiter",3)
    elif (pos.x == house_x and pos.z == house_z+9):
        utils.post_messages(mc,messages,"Overview",3)
    elif (pos.x == house_x+9 and pos.z > house_z+7  and pos.z < house_z+11):
        utils.post_messages(mc,messages,"Atrium",3)
    elif ((pos.x == house_x+12 and pos.z == house_z+5) or
          (pos.x == house_x+16 and pos.z == house_z+5) or
          (pos.x == house_x+17 and pos.z == house_z+5) or
          (pos.x == house_x+19 and pos.z == house_z+5) or
          (pos.x == house_x+36 and pos.z == house_z+4) or
          (pos.x > house_x+24 and pos.x < house_x+27 and pos.z == house_z+4) or
          (pos.x > house_x+30 and pos.x < house_x+33 and pos.z == house_z+4) or
          (pos.x > house_x+14 and pos.x < house_x+17 and pos.z == house_z+14) or
          (pos.x == house_x+28 and pos.z == house_z+16)):
        utils.post_messages(mc,messages,"Cubicula",3)
    elif (pos.x == house_x+28 and pos.z > house_z+11 and pos.z < house_z+14):
        utils.post_messages(mc,messages,"Peristylum",3)
    elif (pos.x < house_x+28 and pos.x > house_x+21 and pos.z > house_z+4 and pos.z < house_z+11):
        utils.post_messages(mc,messages,"Tablinium",3)
    elif (pos.x == house_x+2 and (pos.z == house_z+7 or pos.z == house_z+11)):
        utils.post_messages(mc,messages,"Taberna",3)
    elif (pos.x == house_x+31 and pos.z == house_z+18):
        utils.post_messages(mc,messages,"Toilet",3)
    elif (pos.x > house_x+35 and pos.x < house_x+39 and pos.z == house_z+16):
        utils.post_messages(mc,messages,"Triclinium",3)        
    elif (pos.x>house_x+38 and pos.x<house_x+41 and pos.z == house_z):
        utils.post_messages(mc,messages,"End",3) 
        explosion.explosion(19,  28, -355)
        time.sleep(10)
        explosion.smoke_1(-200, 50, -355, 200, 52, -200)
        break
    
while True:
    explosion.smoke_2(-200, 50, -355, 200, 52, 300)
        

