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
    const [rangeTable, setRangeTable] = useState("")

    const [wrongOptionColor, setWrongOptionColor] = useState("primary")
    const [correctOptionColor, setCorrectOptionColor] = useState("primary")

    function handleCorrect() {
      setCorrectOptionColor("green")
      console.log(correctOptionColor)
      
    }
    
    function handleWrong() {
      setWrongOptionColor("red")
    }
    
    const fetchHand = async () => {
      const response = await fetch("http://localhost:8000/dealHand")
      const result = await response.json()
      setHand(result.hand)
      setPosition(result.position)
      setOptions(result.options)
      setCorrectOption(result.correctOption)
      setRangeTable(result.rangeTable)
    }
    useEffect(() => {
      fetchHand()
    }, [])

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
  
      <p>{hand}</p>
      <p>{position}</p>
     
      <p>{correctOption}</p>
      <Stack spacing={2} direction="column">
        {optionsList}
      </Stack>
      <div>
        {htmlParser.parse(rangeTable)}
      </div>

    </>
  )
}

export default App
