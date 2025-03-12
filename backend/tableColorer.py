import poker
def colorer(red, green, blue, chosenCard):
    fullTable = poker.hand.Range("XX").to_ascii().split()
    output = "<table class='range'>"
    for row in range(13):
        output += "<tr>"
        for col in range(13):
            card = fullTable[row * 13 + col]
            modifiedCard = card
            if card == chosenCard:
                modifiedCard = f"<b>{card}</b>"
  
                
                
            if card in red:
                output += f"<td class='red'>{modifiedCard}</td>"
            elif card in green:
                output += f"<td class='green'>{modifiedCard}</td>"
            elif card in blue:
                output += f"<td class='blue'>{modifiedCard}</td>"
            else:
                output += f"<td>{modifiedCard}</td>"
        
        
        output += "</tr>"
    
    output += "</table>"
    return output
    