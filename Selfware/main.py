class object():
    goal_is_reached = False
    lines = 0

    def __init__(self,name):
        self.name = name
        
    def self_modeling(self): #fix this
        pass

    def env_modeling(self): #fix this
        pass 


    def observation(self): 
        Counter = 0
        try:
            file = open("test.txt","r")
        except:
            print("File not found but make it now")
            file = open("test.txt","w")
        finally:
            file = open("test.txt","r")
            
            Content = file.read()
            CoList = Content.split("\n")
            for i in CoList:
                if i:
                    Counter += 1
                    object.lines = Counter


    def decide(self): 
        if (object.lines == 10):
            return True
        else:
            return False

    def action(self): 
        with open('test.txt', 'a') as f:
            f.write('Create a line {object.lines}\n'.format(object=object))


    def oda(self):
        while(True):
            object.observation(self)
            object.decide(self)
            object.action(self)
            if (object.decide(self)):
                break
        return object.goal_is_reached



new_object = object("robot")
new_object.oda()




