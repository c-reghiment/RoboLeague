
import basebehavior.behaviorimplementation


class NaoExample_x(basebehavior.behaviorimplementation.BehaviorImplementation):


    def implementation_init(self):

        self.nao = self.body.nao(0);
        # To run a Choregraphe behavior, make sure you connect the final output to the onStopped output in Choregraphe (The right side), else it will never finish! 
        self.nao.start_behavior("test-1f16ce", "behavior_1"); # Start the non-blocking call to start a behavior (This Choregraphe behavior is not on the robot!)
        
        
    def implementation_update(self):

        # Wait until it is done
        if not (self.nao.is_behavior_running("test-1f16ce", "behavior_1")): # Use same behavior ID to check if it is done running
            print 'Done';
            self.set_finished();



