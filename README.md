# I.T.A.G.E
**Is This A Game Engine?**

Join me on this quest to make a decent game engine. 

This is still a very crude idea.

I am using pygame for the basic drawing for now. I want to port this to CPP someday and base the rendering on Vulkan maybe.

Any contributions are welcomed!

# How to

The primitive component here is called as "component", the baseclass can be found in `component.py`. Multiple components form a `Screen`. And the `ScreenManager` deals with them.

The `EventHandler` class handles all the events. It checks and processes each `Action` in the current `Screen`. An action is a function that is defined as a function inside each component. The eventhandler gives the event to the action and action has to deal with this.

`main.py` and `mainmenu.py` show some typical code that can be used here.

*I am currently working on adding the basic components that are essential for any engine.*
