#Project Alarm Clock
global r
global c
global cmr
global cmc
global pmr
global pmc
global ii
global jj
global r1
global r2
global r3
global c1
global c2
global c3

global cr1
global cr2
global cr3
global cc1
global cc2
global cc3

cmr=[]#computer move
cmc=[]
pmr=[]#player move
pmc=[]

r1=[]#for rows of player
r2=[]
r3=[]
c1=[]#for columns
c2=[]
c3=[]

cr1=[]#for rows of computer
cr2=[]
cr3=[]
cc1=[]#for columns
cc2=[]
cc3=[]
import random
import sys

gg="x"
hh="o"

#These 2 functions tracks the players moves
#computer made move and player made move
def playermove(r,c):
    global ii
    ii=0
    for ii in range(1):
        pmr.append(r+1)
        pmc.append(c+1) 
        
        wincheak()
    ii=ii+1

def computermove(r,c):
    global jj
    jj=0
    for i in range(1):
        
        cmr.append(r+1)
        cmc.append(c+1)
        comptrack(r,c)
        wincheak()
    jj=jj+1

def end_program():
  quit()

def winningstatment(a):
    if a==1:
        print("\t ********************************")
        print("\t XOXO Tic Tac Toe XOXO")
        print("Heereee Weee have a winnerrrr")
        print("\t\t      The board")  
        print("\t\t\t- - -")
        print("\t\t\t- - -")
        print("\t\t\t- - -")
        print("The thundering feroseous, killer of deamons and goblins")
        print("THE COMPUTER")
        end_program()

    elif a==0:
        print("\t ********************************")
        print("\t XOXO Tic Tac Toe XOXO")
        print("Heereee Weee have a winnerrrr")
        print("\t\t      The board")  
        print("\t\t\t- - -")
        print("\t\t\t- - -")
        print("\t\t\t- - -")
        print("The thundering feroseous, killer of deamons and goblins")
        print("THE PLAYER")
        end_program()

def wincheak():
    global r1
    global r2
    global r3
    global c1
    global c2
    global c3

    global cr1
    global cr2
    global cr3
    global cc1
    global cc2
    global cc3
    a='x'
    b='o'
    c='-'
    a=cmr.sort()
    b=cmc.sort()
    m=pmr.sort()
    n=pmc.sort()
    wnr=0

    print("r=",r1,r2,r3)
    print("c=",c1,c2,c3)
    print("cr=",cr1,cr2,cr3)
    print("cc=",cc1,cc2,cc3)
    if len(cr1)>2:
        winningstatment(0)
        print(1)
    elif len(cr2)>2:
        winningstatment(0)
        print(2)
    elif len(cr3)>2:
        winningstatment(0)
        print(3)

    elif len(cc1)>2:
        winningstatment(0)
        print(1)
    elif len(cc2)>2:
        winningstatment(0)
        print(2)
    elif len(cc3)>2:
        winningstatment(0)
        print(3)

    elif g[0][0]==b and g[1][1]==b and g[2][2]==b:
        winningstatment(0)
        print(6)
    elif g[0][2]==b and g[1][1]==b and g[2][0]==b:
        winningstatment(0)
        print(7)

    if len(r1)>2:
        winningstatment(1)
    elif len(r2)>2:
        winningstatment(1)
    elif len(r3)>2:
        winningstatment(1)

    elif len(c1)>2:
        winningstatment(1)
        print(1)
    elif len(c2)>2:
        winningstatment(1)
        print(2)
    elif len(c3)>2:
        winningstatment(1)
        print(3)

    elif g[2][0]=='a' and g[1][1]=='a' and g[0][2]=='a':
        winningstatment(1)
    elif g[0][0]=='a' and g[1][1]=='a' and g[2][2]=='a':
        winningstatment(1)

def fan1(r,c):
    s='x'
    t='o'
    if (r+1)==1:
        r=0
        i=0
        for i in range(2):
            c=i
            if s in g[r][c] or t in g[r][c]:
                i=i+1
            else:
                printinfo(r,c)
                computermove(r,c)
    else:
        pass

def fan2(r,c):
    s='x'
    t='o'
    if (r+1)==2:
        r=1
        i=0
        for i in range(2):
            c=i
            if s in g[r][c] or t in g[r][c]:
                i=i+1
            else:
                printinfo(r,c)
                computermove(r,c)
    else:
        pass

def fan3(r,c):
    s='x'
    t='o'
    if (r+1)==3:
        r=2
        i=0
        for i in range(2):
            c=i
            if s in g[r][c] or t in g[r][c]:
                i=i+1
            else:
                printinfo(r,c)
                computermove(r,c)
    else:
        rad()

print("\t ********************************")
print("\t XOXO Welcome to Tic Tac Toe XOXO")
print("\t ********************************")
print("\t\t      The board")  
print("\t\t\t- - -")
print("\t\t\t- - -")
print("\t\t\t- - -")
print("\t ********************************")

g=[[' - ',' - ',' - ',"\n"],
   [' - ',' - ',' - ',"\n"],
   [' - ',' - ',' - ',"\n"]]

print(''.join(g[0]+g[1]+g[2]))



def getinfo():

    global r  
    global c
    global pmr
    global pmc
    r=int(input("Enter row:")) 
    c=int(input("Enter column:")) 
    r=r-1
    c=c-1
    playermove(r,c)
    s='x'
    t='o'
    if s in g[r][c] or t in g[r][c]:
        print("String is already present")
        sys.exit("Byeee")
    else:
        g[r][c]=" "+gg+" "
        printinfo(r,c)
        track(r,c)
        print("Players move:",r,c)

def track(r,c):#Treacks r1,r2 for player moves
    global r1
    global r2
    global r3
    global c1
    global c2
    global c3
    if pmr[-1]==1:
        r1.append(1)
    elif pmr[-1]==2:
        r2.append(2)
    elif pmr[-1]==3:
        r3.append(3)

    if pmc[-1]==1:
        c1.append(1)
    elif pmc[-1]==2:
        c2.append(2)
    elif pmc[-1]==3:
        c3.append(3)

def comptrack(r,c):#Tracks r1,r2,r3 for computer moves
    global cr2
    global cr3
    global cc1
    global cc2
    global cc3
    global cmr
    global cmc

    if cmr[-1]==1:
        cr1.append(1)
    elif cmr[-1]==2:
        cr2.append(2)
    elif cmr[-1]==3:
        cr3.append(3)

    if cmc[-1]==1:
        cc1.append(1)
    elif cmc[-1]==2:
        cc2.append(2)
    elif cmc[-1]==3:
        cc3.append(3)

def radlast():
    print("Radlast")
    rows = random.randint(0, 2)
    cols = random.randint(0, 2)
    print("rows=",rows,"col=",cols)
    s='x'
    t='o'
    
    if s not in g[rows][cols] and t not in g[rows][cols]:
        g[rows][cols]=" "+hh+" "
        printinfo(rows,cols)
        computermove(rows,cols)
        print("here")
        sys.exit("Byeee")
        
    else:
        for i in range(3):
            for j in range(3):
                if s not in g[i][j] and t not in g[i][j]:
                    g[rows][cols]=" "+hh+" "
                    printinfo(rows,cols)
                    computermove(rows,cols)
                    print("here lastrange")
                    sys.exit("Byeee")

def rad():
    rows = random.randint(0, 2)
    cols = random.randint(0, 2)
    s='x'
    t='o'
    
    if s not in g[rows][cols] and t not in g[rows][cols]:
        g[rows][cols]=" "+hh+" "
        printinfo(rows,cols)
        computermove(rows,cols)
        print("Rows=",rows,"col=",cols)
        
        
    else:
        rad()

def printinfo(r,c):
    
    print("**********")
    print('\n'.join([' '.join(sublist) for sublist in g]))


def corners():
    global r
    global c
    getinfo()
    printinfo(r,c)
    print("My move")
# If condition to place o in the centre This cheaks the corners and sides for if the user has placed an x
    if  (r+1)!=2 and (c+1)!=2 or (r+1)+(c+1)==3 or (r+1)+(c+1)==5 :
        r=1
        c=1
        g[r][c]=" "+hh+" "
        printinfo(r,c)
        computermove(r,c)
        

#Cheaks if x is in the centre if not it places o in the corners.
    elif (r+1)==(c+1)and ((r+1)and(c+1))==2:
        a=(random.choice([0,2]))
        b=(random.choice([0,2]))
        r=a
        c=b
        
        g[r][c]=" "+hh+" "
        printinfo(r,c)
        computermove(r,c)
    else:
        print("IDK")
    #computermove(r,c)
    print("corners done")
        
def thewin1():
    print("My move")
    print("tw1")
    global r
    global c
    getinfo()
    playermove(r,c)
    printinfo(r,c)
    global pmr
    global pmc
    row=[]
    col=[]
    
    row=sorted(pmr)
    col=sorted(pmc)
    print(pmr)
    print(pmc)
    s='-'
    i=0
    print("row=",row)
    print("Column",col)
    #Cheaks if the first 2 box are filled
    if row[1]-row[0]==1:
        if row[1]+1==3:
            r=2
        elif row[0]-1==1:
            r=0
    elif row[1]-row[0]==2:
        r=1
    else:
        pass
    #Horizontal cheak
    if row[0]==row[1]:
        r=row[1]-1
    else:
        pass

    #column st line detector
    if col[1]-col[0]==1:
        if col[1]+1==3:
            c=2
        elif col[0]-1==1:
            c=0
    elif col[1]-col[0]==2:
        c=1
    else:
        pass
    #horizontal line detector
    if col[0]==col[1]:
        c=col[1]-1
    else:
        pass

    #cheaks if mid is poss
    if row[1]-row[0]==2 and col[1]==col[0]:
        if col[1]==3:
            r=1
            c=2
        elif col[1]==1:
            r=1
            c=0
    else:
        pass
    t='x'
    u='o'
    if t in g[r][c] or u in g[r][c]:
        fan1(r,c)
        fan2(r,c)
        fan3(r,c)
        
    else:
        g[r][c]=" "+hh+" "
        printinfo(r,c)
        computermove(r,c)

#Cheaks if x is in the centre and then performs the function

def thewin():
    print("tw")
    global r
    global c
    global cmr
    global cmc
    getinfo()
    printinfo(r,c)
    row=[]
    col=[]
    row=sorted(cmr)
    col=sorted(cmc)
    s='-'
    i=0
    print("row=",row)
    print("Column",col)
    #Cheaks if the first 2 box are filled
    if row[1]-row[0]==1:
        if row[1]+1==3:
            r=2
        elif row[0]-1==1:
            r=0
    
    #Horizontal cheak
    if row[0]==row[1]:
        r=row[1]
    

    #column st line detector
    if col[1]-col[0]==1:
        if col[1]+1==3:
            c=2
        elif col[0]-1==1:
            c=0
    
    #horizontal line detector
    if col[0]==col[1]:
        c=col[1]
    
       

    #cheaks if mid is poss
    if row[1]-row[0]==2 and col[1]==col[0]:
        if col[1]==3:
            r=1
            c=2
        elif col[1]==1:
            r=1
            c=0
    
    t='x'
    u='o'
    if t in g[r][c] or u in g[r][c]:
        fan1(r,c)
        fan2(r,c)
        fan3(r,c)
        
    else:
        rad()
def corners3():
    print("My move")
    thewin(r,c)
    
def last():
    print("Last")
    global r
    global c
    global cmr
    global cmc
    m=0
    n=0
    getinfo()
    printinfo(r,c)
    row=[]
    col=[]
    row=sorted(cmr)
    col=sorted(cmc)
    s='-'
    u='x'
    t='o'
    i=0
    print("row=",row)
    print("Column",col)
    if s in g[m][n]:
        rad()
        print(" over1")
    else:
        radlast()
#corners3()

def thewin2():
    print("My move \ntw2")
    global r
    global c
    getinfo()
    playermove(r,c)
    printinfo(r,c)
    global pmr
    global pmc
    row=[]
    col=[]
    
    row=sorted(pmr)
    col=sorted(pmc)
    print(pmr)
    print(pmc)
    i=0
    print("row=",row)
    print("Column",col)
    #Cheaks if the first 2 box are filled
    # if row[-1]-row[-3]==2 and col[-1]==col[0]:
    #     if col[-1]==3:
            
    #         r=1
    #         c=2
    #     elif col[-1]==1:
    #         r=1
    #         c=0
    # else:
    #     pass
    # if row[-1]-row[-2]==1:
        
    #     if row[-1]+1==3:
    #         r=2
    #     elif row[-2]-1==1:
    #         r=0
    # else:
    #     pass
    # #Horizontal cheak
    # if row[-2]==row[-1]:
        
    #     r=1
    # else:
    #     pass

    # #column st line detector
    # if col[-1]-col[-2]==1:
    #     if col[-1]+1==3:
    #         c=2
    #     elif col[-2]-1==1:
    #         c=0
    # else:
    #     pass
    # #horizontal line detector
    # if col[-2]==col[-1]:
    #     c=0
    # else:
    #     pass
    print(len(r1),len(r2),len(r3),len(c1),len(c2),len(c3))
    if 2<=len(r1):
        r=0
    elif 2<=len(r2):
        r=1
    elif 2<=len(r3):
        r=2
    if 2<=len(c1):
        c=0
    elif 2<=len(c2):
        c=1
    elif 2<=len(c3):
        c=2
    
    d='-'
    e='x'
    f='o'
    #cheaks if mid is poss
    if d in g[r][c] and e not in g[r][c] and f not in g[r][c]:
        g[r][c]=" "+hh+" "
        printinfo(r,c)
        computermove(r,c)
        print("tw2 here")
        
    elif e in g[r][c] or f not in g[r][c] and d not in g[r][c]:
        rad()
        print("Rad used in t2")



#BOOKMARK
corners()
#runs perfectly
thewin1()
#runs perfectly
thewin()
#FUCK THIS PIECE OF SHIT
thewin2()
#runs perfectly
last()
#keeps on iterating
#radlast()

#Alternate the code such a way that the last move is made

print(pmr)
print(pmc)
#print(cmr)
#print(cmc)
