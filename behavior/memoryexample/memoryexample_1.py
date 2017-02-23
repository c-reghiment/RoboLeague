
import basebehavior.behaviorimplementation
import rospy


class MemoryExample_x(basebehavior.behaviorimplementation.BehaviorImplementation):

    def implementation_init(self):

        self.state = "idle";

    def implementation_update(self):

        if (self.state == "idle"):
            self.state = "putInMemory1";
        
        elif (self.state == "putInMemory1"):
            self.m.add_item("NameOfObject", rospy.Time.now(), "Just a variable"); # You can put in a single variable (in this case a string)
            self.state = "readMemory1";
            
        elif (self.state == "readMemory1"):
            if (self.m.n_occurs("NameOfObject") > 0): # Check if object even exists in memory
                time, item = self.m.get_last_observation("NameOfObject"); # Just get the last variable that was put in the memory with the name "NameOfObjects"
                print item
                
                self.state = "putInMemory2";
            else:
                print 'Could not find item in memory....'
                self.state = "putInMemory2";
        
        elif (self.state == "putInMemory2"):
            self.m.add_item("NameOfObject", rospy.Time.now(), {"Item1" : 0, "Item2": 1}); # Adding a list 
            self.state = "readMemory2";
            
        elif (self.state == "readMemory2"):
            if (self.m.n_occurs("NameOfObject") > 0): # Again checking, just to make sure!
                time, item = self.m.get_last_observation("NameOfObject");
                print item;
            
                self.state = "readMemory3";
            else:
                print 'Weird that it could not find anything in the memory...';
                self.state = "readMemory3";
                
        elif (self.state == "readMemory3"):
            if (self.m.n_occurs("NameOfObject") > 0): # Yes, check it again!
                items = self.m.get_recent_observations("NameOfObject", rospy.Time.now() - rospy.Duration(2)); # Get all the observations from current time - 2 seconds ago
                print type(items); # Prints the type that items is (Spoiler: it's a 'list'
                print items;
                
                self.state = "readMemory4";
            else:
                print 'Like really it is not there?, this is a bad example!';
                self.state = "readMemory4";
                
        elif (self.state == "readMemory4"):
            if (self.m.n_occurs("NameOfObject") > 0): # You guessed it, where are checking again!
                items = self.m.get_observations("NameOfObject"); # Just get all observations ever
                print type(items);
                print items;
                
                self.set_finished();
            else:
                print 'As if this would fail...'
        



