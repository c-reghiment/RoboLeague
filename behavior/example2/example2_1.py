
import basebehavior.behaviorimplementation
import time

class Example2_x(basebehavior.behaviorimplementation.BehaviorImplementation):


    def implementation_init(self):
        print 'This is the init of example 2';
        
        self.state = "start";
        
        
    def implementation_update(self):

        if (self.state == "start"):
            self.currentTime = time.time();
            self.state = "waiting";
            print 'Waiting...'
            
        elif (self.state == "waiting" and time.time() - self.currentTime > 3.0): # We waited at least 3 seconds
            print 'Done waiting (for minimal 3 seconds)'
            self.set_finished();


