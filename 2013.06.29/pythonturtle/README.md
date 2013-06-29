Python Turtle Workshop
============================

# Introduction

Today we're going to learn about programming.  Programming is telling a computer what to do.
We're going to pretend that we're controlling a little turtle crawling on your screen.  As the turtle
crawls, it can leave behind a line, like you would draw with a marker on a whiteboard.  We will be
using a programming language called **Python** to tell the turtle what to do.

# Setup

To use **Python** we need to put it on your computer first.  You should have it installed already, 
so let's check to see if it's already on your computer.

* press the **Start** button
* type in `idle`
* press *Enter*

If you don't have **Python** on your computer.
* go to www.python.org
* click on `DOWNLOAD`
* click on `Python 3.3.2 Windows x86 MSI Installer`
* once the file downloads, click on it
* keep clicking **Next** in the installer until the installation starts
* click **Yes** to allow **Python** to install
* click **Finish**
* now you can start **IDLE**

# Lesson 1

We should now have the *IDLE* window open.  Before we can play with the **Turtle** we need to tell **Python**
to use it.  To do that we "import" a **Python** library.  A library is a bunch of instructions that teach
**Python** how to do new things.

* type in `from turtle import *` and press **Enter**

We just told **Python** to open the **Turtle** library and use all the commands in that library.
Notice that we had to press **Enter**.  We will need to do that after every command we give to
**Python**, that's how it knows to go ahead and do what we told it to do.

    pendown()
    
We just told **Python** to put it's "pen" on it's "whiteboard".  You should now have another window pop up.  
Move your **IDLE** and your **Python Turtle Graphics** windows so you can see them side-by-side.  We now have a 
"whiteboard" on the screen with an arrow in the middle.  That arrow is our turtle.  I don't like the white background,
I want to have a "blackboard", not a "whiteboard".

    bgcolor('black')

We just told our turtle to draw on a black background, but it's still using the black color for our turtle.

* What do you think happens when we draw now?

    color('red')
    width(3)
    
Now we picked a thicker "marker" to draw with, we also made the marker a little thicker so we can see our lines better.

* What do you think the line thikness starts out as?


