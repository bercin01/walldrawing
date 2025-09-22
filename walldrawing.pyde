def setup():
    size (500,500)
    background(100,50,100)
    
    
    for i in range(1,13):
        line(250,250,random(0,500),random(0,500))
        #linje fra centrum
        
    for i in range(0,13):
        line(0,0,random(0,500),random(0,500))
        
    for i in range(0,13):
        line(0,500,random(0,500),random(0,500))
    
    for i in range(0,13):
        line(500,0,random(0,500),random(0,500))
    
    for i in range(0,13):
        line(500,500,random(0,500),random(0,500))
    
    for i in range(0,13):
        line(250,0,random(0,500),random(0,500))
    
    for i in range (0,13):
        line (250,500,random(0,500),random(0,500))
    
    for i in range (0,13):
        line (0,250,random(0,500),random(0,500))

    for i in range (0,13):
        line(500,250,random(0,500),random(0,500))
