import math
import time
import pandas

def draw_disc(mc,radius,cx,cy,cz,block):
    for i in range(radius*2-1):
        for a in range(radius*2-1):
            side_1 = radius-a
            side_2 = radius-i
            hypotenuse = math.sqrt(side_1**2+side_2**2)
            if (hypotenuse<radius):
                mc.setBlocks(cx-side_1,cy,cz-side_2,cx+side_1,cy,cz-side_2,block)
                break
                    
def draw_ring(mc,radius, width,cx,cy,cz,block):
    for i in range(radius*2-1):
        for a in range(radius*2-1):
            side_1 = radius-a
            side_2 = radius-i
            hypotenuse = math.sqrt(side_1**2+side_2**2)
            if (hypotenuse<radius and hypotenuse > radius - width):
                if(mc.getBlock(cx-side_1,cy,cz-side_2) != block):
                    mc.setBlock(cx-side_1,cy,cz-side_2, block)

def read_info(file):
    messages = {}
    f = open(file, "r")
    for line in f.readlines():
        key = line.split("|")[0]
        msg = line.split("|")[1].strip()
        if not (key in messages):
            messages[key] = list()
        messages[key].append(msg)
    return messages

def say(phrase):
    import os
    os.system("say %s" % phrase)

def post_messages(mc,messages_dictionary,location,delay):
    for msg in messages_dictionary[location]:
        mc.postToChat(msg)
        say(msg)
        time.sleep(delay)
    
                    
def info_recall(mc,file, delay):
    f = open(file, "r")
    for line in f.readlines():
         mc.postToChat(line)
         time.sleep(delay)

def info_recall_tsv(mc,file,delay):
    pd.read_csv(file, sep='\t')
    
