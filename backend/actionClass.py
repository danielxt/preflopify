from tableColorer import colorer
class ActionClass:
    def __init__(self, position, optionsToRange):
        self.position = position
        self.optionToRange = optionsToRange 
        self.optionToRange["Fold"] = []
        
    def getCorrectAction(self, chosenCard):
        
        for option, range in self.optionToRange.items():
   
            if chosenCard in range:
                return option
        return "Fold" # if wasnt defined
        
    def getColoredTable(self, chosenCard):
        red = []
        green = []
        blue = []
        for option in self.optionToRange.keys():
            if option in ["Raise", "Raise for Value"]: # need to extend for vs 3 bet / facing rfi
                red = self.optionToRange[option]
            elif option in ["Limp", "Call"]:
                green = self.optionToRange[option]
            elif option in ["Raise as a Bluff", " 3-bet as a Bluff"]: # need to extend
                blue = self.optionToRange[option]
                
        return colorer(red, green, blue, chosenCard)