import { useEffect, useState, createContext, useCallback } from "react";
import './App.css'


function App() {
    const [hand, setHand] = useState("")
    const [position, setPosition] = useState("")
    const [options, setOptions] = useState([])
    const [correctOption, setCorrectOption] = useState("")
    
    const fetchHand = async () => {
      const response = await fetch("http://localhost:8000/dealHand")
      const result = await response.json()
    
      setHand(result.hand)
      setPosition(result.position)
      setOptions(result.options)
      setCorrectOption(result.correctOption)
    
      

      
      
    }
    useEffect(() => {
      fetchHand()
    }, [])


    const optionsList = options.map(option => <button>{option}</button>)

  return (
    <>
  
      <p>{hand}</p>
      <p>{position}</p>
      <p>{optionsList}</p>
      <p>{correctOption}</p>

    </>
  )
}

export default App
