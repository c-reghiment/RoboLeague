
import basebehavior.behaviorimplementation


class Example3_x(basebehavior.behaviorimplementation.BehaviorImplementation):

    def implementation_init(self):

        self.state = "goingToFail";

    def implementation_update(self):

        if (self.state == "goingToFail"):
            self.set_failed("I failed for some reason"); # You can give different reasons that you can use in your main behavior for making the next choice.

