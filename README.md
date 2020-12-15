# CSE-571-Final-Project

For our final project, a team of two and I implemented bidirectional search in the Pacman domain. Bidirectional search utilizes two A* searches. One from the beginning, and another from the end. The search is completed once the two "meet in the middle". This search has been implemented as described in the paper, 
*[Bidirectional Search That Is Guaranteed to Meet in the Middle](https://people.engr.tamu.edu/guni/Papers/AAAI16-MM.pdf)*. A diagram illustrating the process can be seen below:

![pacman Domain](https://i.imgur.com/w9XlrDR.png)


This Pacman domain is a simple food search problem. The Pacman explores the maze searching for a single goal node such as is shown below. The darker red is paths explored sooner on in the lifetime of the agent. 

![pacman Domain](https://i.imgur.com/0ZlCjHl.gif)



We have completed an analysis of this algorithm and compared it with other search methods such as DFS, BFS, and UCS. All of our analysis can be found in the [Final_Report.pdf](https://github.com/forksup/CSE-571-Final-Project/blob/main/Final_Report.pdf)
