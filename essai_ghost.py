from pyamaze import maze,agent,COLOR,textLabel
from queue import PriorityQueue
def killAgent(k):
        for i in range(len(k._body)):
                m._canvas.delete(k._body[i])
        m._canvas.delete(k._head) 
        

def h(cell1, cell2): #manhatten distance
    x1, y1 = cell1
    x2, y2 = cell2
    return (abs(x1 - x2) + abs(y1 - y2))


def aStar(ghosts_pos,m,start=None):
    if start is None:
        start=(m.rows,m.cols)      
    open = PriorityQueue()        
    open.put((h(start, m._goal), h(start, m._goal), start))    
    aPath = {}                     
    g_score = {row: float("inf") for row in m.grid}      
    g_score[start] = 0
    f_score = {row: float("inf") for row in m.grid} 
    f_score[start] = h(start, m._goal)
    searchPath=[start]
    while not open.empty():       
        currCell = open.get()[2]
        searchPath.append(currCell)   
        if currCell == m._goal:
            break           
        for d in 'ESNW':
            if m.maze_map[currCell][d]==True:           
                if d=='E':
                    childCell=(currCell[0],currCell[1]+1)
                elif d=='W':
                    childCell=(currCell[0],currCell[1]-1)
                elif d=='N':
                    childCell=(currCell[0]-1,currCell[1])
                elif d=='S':
                    childCell=(currCell[0]+1,currCell[1])
                if childCell not in ghosts_pos:
                    temp_g_score = g_score[currCell] + 1
                    temp_f_score = temp_g_score + h(childCell, m._goal)

                    if temp_f_score < f_score[childCell]:     
                        aPath[childCell] = currCell
                        g_score[childCell] = temp_g_score
                        f_score[childCell] = temp_g_score + h(childCell, m._goal)
                        open.put((f_score[childCell], h(childCell, m._goal), childCell))  
                         
                

                


    fwdPath={}
    cell=m._goal
    while cell!=start:
        fwdPath[aPath[cell]]=cell
        cell=aPath[cell]
    return searchPath,aPath,fwdPath

if __name__=='__main__':
    m=maze(7,7)
    m.CreateMaze(loadMaze='aStardemo.csv')

    ghosts=list()
    ghost1=agent(m,5,7,shape='arrow',footprints=True)
    
    ghost2=agent(m,5,3,shape='arrow',footprints=True)
   

    ghost3=agent(m,2,2,shape='arrow',footprints=True)
    
    
    

    ghosts.append(ghost1.position)
    ghosts.append(ghost2.position)
    ghosts.append(ghost3.position)
  

    goals={}

    goal1=agent(m,1,7,shape='arrow',color=COLOR.red,footprints=True)
    #goal1.position=(1,7)
   
    goal2=agent(m,3,3,shape='arrow',color=COLOR.red,footprints=True)

    goal3=agent(m,5,1,shape='arrow',color=COLOR.red,footprints=True)
    #goal2.position=(1,1)
 
    goal4=agent(m,1,1,shape='arrow',color=COLOR.red,footprints=True)
    #goal2.position=(1,1)
 

    

    goals[goal1.position]=goal1
    goals[goal2.position]=goal2
    goals[goal3.position]=goal3
    goals[goal4.position]=goal4
    
    temps=0

    deb=(7,7)

    for i,k in goals.items():
        x,y=i[0],i[1]   #goal
        m._goal=(x,y)
        searchPath,aPath,fwdPath=aStar(ghosts,m,deb)
        temps+=len(fwdPath)
       
        
        
        pacman=agent(m,deb[0],deb[1],color=COLOR.yellow)
        m._canvas.delete(pacman._head)
        m.tracePath({pacman:fwdPath},kill=True,delay=300)
        m._win.after(300*temps, killAgent,k)
        
   
        
        deb=i
        l=textLabel(m,'A Star Search Length',len(searchPath))
    

    
    
    
    m.run()
   
# a=agent(m,7,7,footprints=True,color=COLOR.blue,filled=True)
#m.tracePath({a:searchPath},delay=200)
#b=agent(m,1,7,footprints=True,color=COLOR.red,filled=True,goal=(7,7))
# # m.tracePath({b:aPath},delay=200)

    
   
