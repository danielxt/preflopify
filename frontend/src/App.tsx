import { useEffect, useState} from "react";
import './App.css'
import { Parser } from "html-to-react";
import Stack from '@mui/material/Stack';
import Button from '@mui/material/Button';
import { Typography } from "@mui/material";
import { Container } from "@mui/material";
import RestartAltIcon from '@mui/icons-material/RestartAlt';
import Grid from '@mui/material/Grid2';

import SimpleBackdrop from './Backdrop.tsx'


function App() {
    const [hand, setHand] = useState("")
    const [position, setPosition] = useState("")
    const [options, setOptions] = useState([])
    const [correctOption, setCorrectOption] = useState("")
    const htmlParser = Parser();
    const [blankRangeTable, setBlankRangeTable] = useState("")
    const [coloredRangeTable, setColoredRangeTable] = useState("")
    const [scenario, setScenario] = useState("")

    const [wrongOptionColor, setWrongOptionColor] = useState("primary")
    const [correctOptionColor, setCorrectOptionColor] = useState("primary")

    const [madeChoice, setMadeChoice] = useState(false)

    


    function handleAnswer() {
      if (!madeChoice) {
        setCorrectOptionColor("#81c784")
        setWrongOptionColor("#e57373")
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
      setScenario(result.scenario)
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
          return <Button key={option} sx={{bgcolor: `${correctOptionColor}`}}  variant="contained" onClick={() => handleAnswer()}>{option}</Button>
        }
        else {
          return <Button key={option} sx={{bgcolor: `${wrongOptionColor}`}} variant="contained" onClick={() => handleAnswer()}>{option}</Button>
         
        }
     
       
      }
    
     
        
  
       

      

    )

  return (
   
    <Container maxWidth="sm">
      <Grid container padding={1} borderBottom={"1px solid grey"}>
        <Grid size={4}>
          <Typography variant="h4"><b>Preflopify</b></Typography>
        </Grid>
        <Grid size={8}>
          <Typography align="right"><SimpleBackdrop/></Typography>
        </Grid>
  
      </Grid>

      
      <Stack sx={{bgcolor:'secondary'}} padding={1} borderRadius="10px" margin={1}>
        {htmlParser.parse(rangeTable)}
      </Stack>
      <Typography>
        {scenario}
      </Typography>
      <Typography variant="h5"><b>Dealt {hand} in {position}</b></Typography>

      <Stack spacing={1} direction="column" sx={{bgcolor:'dark'}} borderRadius="10px" padding={2}>
        {optionsList}
        <Button variant="outlined" onClick={() => reset()}><RestartAltIcon/></Button>
      </Stack>

    </Container>
     
      

   
  )
}

export default App
