
import basebehavior.behaviorimplementation


class ExampleMain_1(basebehavior.behaviorimplementation.BehaviorImplementation):

    def implementation_init(self):
        
        self.state = "idle";
        
        # Sub-behaviors
        self.CreateExample2();
        self.CreateExample3();
        self.CreateExample4({});
        
        
        # Init variables
        self.startExample2 = False;
        self.startExample3 = False;
        self.startExample4 = False;
        
        # Starting conditions of sub-behaviors
        self.selected_behaviors = [
            ("example2", "self.startExample2 == True"),
            ("example3", "self.startExample3 == True"),
            ("example4", "self.startExample4 == True")            
            ]
        
    def CreateExample2(self):
        self.example2 = self.ab.example2({});
    
    def CreateExample3(self):
        self.example3 = self.ab.example3({});
    
    def CreateExample4(self, param):
        self.example4 = self.ab.example4({'variableToPass' : param});
        

    def implementation_update(self):
        
        # You could print the state the system is in to help with debugging.
        #print self.state 

        if (self.state == "idle"):
            self.state = "startExample2";
            
        # This might seem silly, but if you make a start state for each sub-behaviour, it will be easier for debugging only a part of your system
        elif (self.state == "startExample2"):
            self.CreateExample2();
            self.startExample2 = True;
            self.state = "runningExample2";     
            
        elif (self.state == "runningExample2" and self.example2.is_finished()): # the sub-behavior is done
            print 'Example2 sub-behavior is done';
            self.startExample2 = False;
            self.state = "startExample3";
        
        
        elif (self.state == "startExample3"):
            self.CreateExample3();
            self.startExample3 = True;
            self.state = "runningExample3";
        
        elif (self.state == "runningExample3" and self.example3.is_finished()): # Should never get here though, cause it should always fail
            print "This should not have happened....";
            self.startExample3 = False;
            self.set_failed("Something weird happened");
            
        elif (self.state == "runningExample3" and self.example3.is_failed()): # Failed sub-behavior
            print "Reason for failing: ", self.example3.get_failure_reason();
            self.startExample3 = False;
            self.state = "startExample4";
            
        elif (self.state == "startExample4"):
            self.CreateExample4("This is a variable");
            self.startExample4 = True;
            self.state = "runningExample4";
            
        elif (self.state == "runningExample4" and self.example4.is_finished()): # Should only get here, not trying for failed this time...
            self.startExample4 = False;
            self.state = "Done";
            
        elif (self.state == "Done"):
            self.set_finished();
            
            
            