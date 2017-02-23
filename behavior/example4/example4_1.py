
import basebehavior.behaviorimplementation


class Example4_x(basebehavior.behaviorimplementation.BehaviorImplementation):


    def implementation_init(self):
        
        if not hasattr(self, "variableToPass"):
            self.variableToPass = "defaultValue";
            
        print self.variableToPass;
        self.set_finished();
        

    def implementation_update(self):

        pass



