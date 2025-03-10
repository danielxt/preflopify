import { useEffect, useState, createContext } from "react";
import './App.css'


interface Hand {
  value: string
}

const HandContext = createContext({
  hand: "", fetchHand: () => {}
})

function App() {
    const [hand, setHand] = useState("")
    const fetchHand = async () => {
      const response = await fetch("http://localhost:8000/getRandomHand")
      const hand = await response.json()
      setHand(hand.data)
      setHand(hand.value)
      
    }
    useEffect(() => {
      fetchHand()
    }, [])


  return (
    <>
      <HandContext.Provider value={{hand, fetchHand}}>
        
      <p>{hand}</p>

      </HandContext.Provider>
    </>
  )
}

export default App
