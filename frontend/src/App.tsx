import { useEffect, useState, createContext, useCallback } from "react";
import './App.css'
import { Parser } from "html-to-react";
import Stack from '@mui/material/Stack';
import Button from '@mui/material/Button';




function App() {
    const [hand, setHand] = useState("")
    const [position, setPosition] = useState("")
    const [options, setOptions] = useState([])
    const [correctOption, setCorrectOption] = useState("")
    const htmlParser = Parser();
    const [blankRangeTable, setBlankRangeTable] = useState("")
    const [coloredRangeTable, setColoredRangeTable] = useState("")

    const [wrongOptionColor, setWrongOptionColor] = useState("primary")
    const [correctOptionColor, setCorrectOptionColor] = useState("primary")

    const [madeChoice, setMadeChoice] = useState(false)

    


    function handleCorrect() {
      if (!madeChoice) {
        setCorrectOptionColor("green")
        setMadeChoice(true)
      }
      
      
    }
    
    function handleWrong() {
      if (!madeChoice) {
       
        setWrongOptionColor("red")
        setMadeChoice(true)
      }
      
    }

    function reset() {
      setCorrectOptionColor("primary")
      setWrongOptionColor("primary")
      setMadeChoice(false)
      fetchHand()
    }
    
    const fetchHand = async () => {
      const response = await fetch("http://localhost:8000/dealHand")
      const result = await response.json()
      setHand(result.hand)
      setPosition(result.position)
      setOptions(result.options)
      setCorrectOption(result.correctOption)
      setBlankRangeTable(result.blankRangeTable)
      setColoredRangeTable(result.coloredRangeTable)
    }
    useEffect(() => {
      fetchHand()
    }, [])

    var rangeTable = ""
    if (madeChoice) {
      rangeTable = coloredRangeTable
    }
    else {
      rangeTable = blankRangeTable
    }

    const optionsList = options.map(
    (option) => 
      {

        if (option == correctOption) {
          return <Button key={option} sx={{bgcolor: `${correctOptionColor}`}}  variant="contained" onClick={() => handleCorrect()}>{option}</Button>
        }
        else {
          return <Button key={option} sx={{bgcolor: `${wrongOptionColor}`}} variant="contained" onClick={() => handleWrong()}>{option}</Button>
         
        }
     
       
      }
    
     
        
  
       

      

    )

  return (
    <>
  
      
      <div>
        {htmlParser.parse(rangeTable)}
      </div>

      <b>Dealt {hand} in {position}</b>

      <Stack spacing={1} direction="column">
        {optionsList}
        <Button variant="contained" onClick={() => reset()}>Reset</Button>
      </Stack>

      

    </>
  )
}

export default App
