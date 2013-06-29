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

Let's draw some stuff now.

        forward(50)

Hey, we have a line!  We can't just keep doing in straight line, we need to turn our turtle:

        right(90)
        
Our turtle turned to the right, but why 90?  We need to tell our turtle how much to turn by.  To do that we divide the circle
into 360 even slices.  Now we can tell the turtle exactly how much to turn.

        fd(200)

We got another line, but this time we're lazy, so we won't type out `forward`, we can just say `fd`.

        left(90)
        fd(50)
        left(90)
        color('green')
        fd(100)
        color('white')
        fd(100)
        width(10)
        go(100)
        left(90)
        width(1)
        go(100)
        width(50)
        go(100)

# Lesson 2

        reset()
        color('red')
        fd(50)
        right(90)
        hideturtle()
        fd(100)
        showturtle()
        right(90)
        penup()
        fd(100)
        right(90)
        pendown()
        fd(50)
        
        clear()
        fd(100)

# Lesson 3

        reset()
        from turtle import *
        pendown()
        bgcolor('black')
        width(3)
        
        color('red')
        for i in range(3):
            fd(100)
            right(360/3)
        
        color('white')
        for i in range(4):
            fd(100)
            right(360/4)
        
        color('blue')
        for i in range(5):
            fd(100)
            right(360/5)
        
        left(90)
        for i in range(40):
            width(i)
            fd(4)
        
        color('red')
        width(3)
        for i in range(36):
            fd(10)
            right(10)

# Lesson 4

        reset()
        
        for i in range(36):
            for j in range(36):
                fd(10)
                right(10)
            right(10)
            
        clear()
        
        def polygon(n):
        for i in range(n):
            fd(50)
            right(360.0/n)
        
        polygon(5)
        
        for i in range(3,10):
            polygon(i)
        
        clear()
        for i in range(3,15):
            polygon(i)
            right(30)
        
        clear()
        
        def circle():
            for i in range(36):
                fd(10)
                right(10)
        
        color_list=['red', 'green', 'blue', 'purple', 'orange', 'yellow']
        for item in color_list:
            color(item)
            circle()
            right(60)
