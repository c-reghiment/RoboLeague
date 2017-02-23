
import basebehavior.behaviorimplementation


class ExampleMain_1(basebehavior.behaviorimplementation.BehaviorImplementation):

    def implementation_init(self):
        
        self.state = "idle";
        
        # Sub-behaviors
        self.CreateSearchBall();
        self.CreateApproachBall();
        self.CreateKickBall({});
        
        
        # Init variables
        self.startSearchBall = False;
        self.startApproachBall = False;
        self.startKickBall = False;
        
        # Starting conditions of sub-behaviors
        self.selected_behaviors = [
            ("SearchBall", "self.startSearchBall == True"),
            ("ApproachBall", "self.startApproachBall == True"),
            ("KickBall", "self.startKickBall == True")            
            ]
        
    def CreateSearchBall(self):
        self.SearchBall = self.ab.SearchBall({});
    
    def CreateApproachBall(self):
        self.ApproachBall = self.ab.ApproachBall({});
    
    def CreateKickBall(self, param):
        self.KickBall = self.ab.KickBall({'variableToPass' : param});
        

    def implementation_update(self):
        
        # You could print the state the system is in to help with debugging.
        #print self.state 

        if (self.state == "idle"):
            self.state = "startSearchBall";
            
        # This might seem silly, but if you make a start state for each sub-behaviour, it will be easier for debugging only a part of your system
        elif (self.state == "startSearchBall"):
            self.CreateSearchBall();
            self.startSearchBall = True;
            self.state = "runningSearchBall";     
            
        elif (self.state == "runningSearchBall" and self.SearchBall.is_finished()): # the sub-behavior is done
            print 'SearchBall sub-behavior is done';
            self.startSearchBall = False;
            self.state = "startApproachBall";
        
        
        elif (self.state == "startApproachBall"):
            self.CreateApproachBall();
            self.startApproachBall = True;
            self.state = "runningApproachBall";
        
        elif (self.state == "runningApproachBall" and self.ApproachBall.is_finished()): # Should never get here though, cause it should always fail
            print "This should not have happened....";
            self.startApproachBall = False;
            self.set_failed("Something weird happened");
            
        elif (self.state == "runningApproachBall" and self.ApproachBall.is_failed()): # Failed sub-behavior
            print "Reason for failing: ", self.ApproachBall.get_failure_reason();
            self.startApproachBall = False;
            self.state = "startKickBall";
            
        elif (self.state == "startKickBall"):
            self.CreateKickBall("This is a variable");
            self.startKickBall = True;
            self.state = "runningKickBall";
            
        elif (self.state == "runningKickBall" and self.KickBall.is_finished()): # Should only get here, not trying for failed this time...
            self.startKickBall = False;
            self.state = "Done";
            
        elif (self.state == "Done"):
            self.set_finished();
            
            
            