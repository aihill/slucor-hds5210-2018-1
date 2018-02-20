class Room():
    """
    A Room is a specific place identified by the building and room number that tells us where it can be found.
    We can create new instances of a Room by passing in either the building name and room number as separate
    parameters or by passing in a single string in the format "<building> <number>".  See the examples.
    
    attributes: building, room_nbr
    """
    
    def __init__(self,label):
        """
        This initialization method will create a new Room object based on a string in the format "<building> <number>".
        
        >>> Room('Salus 1481')
        """
        self.building = label[0:label.find(' ')]
        self.room_nbr = label[label.find(' ')+1:]
        self.label = label
        
        