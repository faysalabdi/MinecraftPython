# MinecraftPython

Minecraft Procedural Village Generator Project

## Overview:
This project involves developing a Python script that procedurally generates a "block world" village in Minecraft using Minecraft's Python API, MCPI. The main goal is to create a unique and creative village layout while adhering to specific constraints.

## Key Components:

Landscaping: Create randomized, flat plots of land for house construction while maintaining the natural terrain features.
Road Network: Connect the plots with a road network, taking into consideration random house locations and avoiding steep roads or underwater paths.
Houses: Develop a procedural house generator that builds houses with walls, windows, a roof, and a main door. More complex houses with multiple rooms and stories are encouraged.
Additional Structures: Enhance the village by adding features such as swimming pools, furniture, streetlamps, gardens, statues, and wells.
Requirements:

Use appropriate data structures or object-oriented programming concepts for each component.
Create a short video presentation explaining the implementation and justifying the chosen data structures or object-oriented design.
Participate in group consultations with teaching staff.
This project aims to refresh Python programming skills and familiarize students with high-level API development while encouraging creativity in village design and layout.


## Development Diary

**Week 1**
* Faysal Abdiwahab (s3783895)
    * Read chapter 1 & 2 on textbook
    * Setup Minecraft server
    * Implemented Hello Minecraft!
    * Did some coding examples from the Minecraft Pi website 
    * Completed in class activities. Became adjusted with the API
    * Began working on Assignment 1 -
        * Created a basic house
        * Moved on to creating a basic double story house
        * Added some basic furniture
        * Began randomising the dimensions of house 
        * Aim for next week is to fully randomise dimensions of house and create templates 

* Ishmam Yasar (s3791863)
    * Read chapter 1 & 2 on textbook
    * Setup VS Code, and Minecraft on Windows 11
    * Iplemented Hello Minecraft!
    * Read through the links provided to get a better understanding of the functions such as setBlock.
    * Did some activities such as buildig stairs to get more familiarize with python in Minecraft.
    * Started of Assignment 1 by testing out a basic fucntion to create a flat land
         * created basic pillars
         * created a basic plot of top of the pillars
         * randomized the hight of the pillars 
         * hardcode randomising of the pillar location
         
* Ahamd Akkad (s3920007)
    * Read chapter 1 & 2 on textbook
    * Setup VS Code, and Minecraft on Mac OS
    * Implemented Hello Minecraft!
    * Went through a few YouTube videos to familiarise myself with Minecraft Pi Edition API
    * Went through some activities such as building stairs using a for loop and recursively.
    * I started Assignment 1 by thinking of an approach to create a path that connects to all houses.

* Student 4
    * Read chapter 1 & 2 on textbook
    * Setup VS Code on Windows, as well as Minecraft Pi on Raspberry Pi OS (on Raspberry Pi 400)
    * Implemented Hello Minecraft!

**Week 2**
* Faysal Abdiwahab (s3783895)
    * Continuing Assignment 1
      * Created a list of materials for house parts , randomly select materials by using a random function to loop through the list. 
      * Created second story and implemented feature to only build second story if house is past certain height. 
      * Created stairs leading up to second story 
      * Started function for generating rooms within house 
      
* Ishmam Yasar (s3791863)
   * Tried the approach of placing plots on deafult hills
   * Reverted back to the original plan of ceating a carpark
   * used a for loop to place pillars on 2 sides with random height and random vertical and horizontal gaps between each pillar
   * created a tree hoouse like structure with branches that have the size randomized to representing the height.
   * placed plots with random width and lengthon top of the pillars.
   * created some additional structures such as trees, garden, pools.

* Ahamd Akkad (s3920007)
    * I now came up with two ways to create a path between the houses.
    * The simpler one was to create on the main strip and make a bridge that connects to all houses.
    * The other option was to learn about graph algorithms and try and implement A* or Dijkstra's Algorithms.
    * I went with the second option since I still have time to change plans if I found implementing graph algorithms too hard.
    * I started watching videos on YouTube on Graph Algorithms, and their representations and terminologies.
    * I also watched videos about Single Source Shortest Path Problem (SSSPP), and Dijkstra's Algorithm for SSSP.
    * I will try to implement Dijkstra's Algorithms if it's within my ability to do so.
    
**Week 3**
* Faysal Abdiwahab (s3783895)
* Read chapters on memory and CPU 
* Completed participation questions

* Created rooms for houses which are generated somewhat randomly based on the dimensions of the house (e.g if house has x height there is room upstairs) 

    * This room function only creates one additional room on each story however, (2 rooms / story) Would add more but since the requirement has been met, ill leave it as is.

    * Attempted to convert my function into a class and use it to subdivide the house into rooms recursively. I found this quite challenging so for now I'll forget it.

* Houses can now be generated randomly with random materials as well as rooms inside. I have also implemented a feature to flip the orientation of the houses to adapt to the road network. 

* House file contains a bunch of functions without any classes or OOP. Had I started with using classes instead of hard coding, I would not have run into my current problem; which is trying to conver all my code into a more object oriented approcach. My attempt at doing this conversion led to running into a lot of bugs, and since the deadline is approaching I have ultimately decided to just leave it as it is.

Ishmam Yasar s3791863

   Not using classes from the beginning came with its challenges as I only had a few days left but I didn’t give up and with the help of my teammates we pulled through. 
   
   I decided to do object-oriented design, canter of focus being the pillars, I created 2 classes, Pillar and Plot. The fist inclusive of the different functions I need to set a basic framework of a pillar and testing some functions such as intersects and generateRandomPillar to avoid pillars overlapping, which were ultimately not used, as the randomized gap was large enough to make sure pillars don’t intersect. I also assigned x, y, z, length and with variables
   
  I made a function to clear land, place a flat car park like structure at the same height and filled in the land underneath to avoid the flat structure from floating.
   
   The plot class basically creates a bunch of plots all with random x -z locations, length, width and height. Creating a total oof 8 random plots 4 on each side of the centre gap reserved for the path, using for loops one that will enable the 2nd for loop to run 2 times for each side. for which I created a build function.

   Initially the plan was to incorporate hills surrounding the flat land, fences, trees and pools but found it to be time consuming and since we were coming to an end so I decided to avoid it.


Ahamd Akkad (s3920007)

   * After trying to implement Dijkstra’s Algorithm, I found it too hard to implement. I ran into many issues and bugs, so I decided to go back to my other idea, which is having one main path and creating a bridge that connects each door to the main strip of the path.

   * I assumed that I have the coordinates for the doors.
    Then I created a function to calculate the distances of any two coordinates. The function was used alongside a nested for loop to find the further two doors away from each other to locate the main path's start and end coordinate of the main path.

   * To find the most suitable width for the main path I found the nearest door of each of the main paths, I found the nearest door of each of the two furthest houses. Then I got the average (x,z) coordinates to finalize the start and the end of the path.
    I calculated the Y-coordinates of the main path by getting the average Y-coordinate of each door.
    To connect the main path to each door I had first created an array that has each coordinate of the main path.

    * Then I found the nearest block from the main path that is closest to each door.
    Then I looped through each door with 12 different block placements to find which placement is closest to the path. This was looped until each door was connected to the main patth.
    

     

    

