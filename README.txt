# README

The code and other files in this repository are part of a project my son (9) did for his school homework September-October 2017. The project was to recreate some part of Pompeii and the eruption of Vesuvius in Minecraft, which has been achieved through the use of the code distributed alongside the "Adventures in Minecraft" book by Martin O'Hanlon and David Whale and in particular on a Mac.

I worked with him on the project, but the majority of the work was done by him, with me offering support, guidance, and some (but by no means the majority) of the code. For more information about the project, see his presentation about the project available at <https://youtu.be/BKmO1pvL2YY>.

You can use this code by downloading the Adventures in Minecraft code from http://media.wiley.com/assets/7266/44/AIMStarterKitMac.zip, and putting the python code from this repository into the "My Adventures" folder, and (once you have a Minecraft server running with the Raspberry Juice plugin running), then running the "play.py" program.

You can see the results of running the program in a screencast made by my son at <https://youtu.be/C84f9UvT7V8>.

The code has only been tested on Mac using the Bukkit Minecraft server running Minecraft 1.6.4; the Raspberry Juice plugin; and Python 2.7. Because of the differences in support for specific blocks/block parameters across Minecraft versions and across platforms, it may not work on all versions of Minecraft which work with the mcpi library.

The code assumes you are working in a newly spawned 'super flat' Minecraft world - so it doesn't clear any space etc. before it builds.

This repository has three folders/directories:

- **python_code**: this is the python code that will create parts of Pompeii and Vesuivius in Minecraft. It requires the mcpi library including the 'minecraftstuff.py' code - which can be downloaded from https://github.com/AdventuresInMinecraft/AdventuresInMinecraft-Mac/tree/master/MyAdventures/mcpi
- **planning**: this contains a spreasheet (and a PDF created from it) which we used to plot out the floor plan for the most complex building that is built in the code
- **scripts_and_properties**: We made some minor modifications to the script which starts and stops the Minecraft server and some of the server properties. You can replace the default files from the Adventures in Minecraft download with these updated versions if you wish:
  - StartBukkit.command: edited to ensure that when you restart Minecraft, it spawns a new world (by moving the existing world directory in Bukkit directory)
  - server.properties: edited so a Superflat world is spawned when starting Bukkit
  - start_server.command: edited to allocate 4Gb RAM to Minecraft

