import { useEffect, useState} from "react";
import './App.css'
import { Parser } from "html-to-react";
import Stack from '@mui/material/Stack';
import Button from '@mui/material/Button';
import { Typography } from "@mui/material";
import { Container } from "@mui/material";
import RestartAltIcon from '@mui/icons-material/RestartAlt';
import Grid from '@mui/material/Grid2';
import Box from "@mui/material";
import clickSound from './assets/click.mp3'
import SimpleBackdrop from './Backdrop.tsx'
import InfoIcon from '@mui/icons-material/Info';
import useSound from 'use-sound';
import successSound from './assets/success.mp3'
import failSound from './assets/fail.mp3'
import HelpOutlineIcon from '@mui/icons-material/HelpOutline';


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
    const [success] = useSound(successSound);
    const [fail] = useSound(failSound)
    const [click] = useSound(clickSound)
    function correctAnswer() {
      success()
      handleAnswer();
    }

    function failAnswer() {
      fail()
      handleAnswer()
    }

    function handleAnswer() {
      if (!madeChoice) {
        setCorrectOptionColor("#81c784")
        setWrongOptionColor("#e57373")
        setMadeChoice(true)
      }
      
      
    }
    
    

    function reset() {
      click()
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
          return <Button key={option} sx={{bgcolor: `${correctOptionColor}`}}  variant="contained" onClick={() => correctAnswer()}>{option}</Button>
        }
        else {
          return <Button key={option} sx={{bgcolor: `${wrongOptionColor}`}} variant="contained" onClick={() => failAnswer()}>{option}</Button>
         
        }
     
       
      }
    )

    const infoText = (
      <Grid container>
         
       <Typography variant="h4">
        <b>What is Preflopify?</b>
      </Typography>

    
      </Grid>
     
    );
    const scenarioText = (
      <Typography>
      Scenario: <b>{scenario} </b> 
    </Typography>
    
    )

    var scenarioTextMeaning;
    if (scenario === "Raise First In") {
      scenarioTextMeaning = 
        <p>
        <b>Raise First In/RFI: </b> Raising first into the pot. Occurs when all players before you have folded and you decide to raise.
        </p>
    }
    else if (scenario == "Facing 3bet") {
      scenarioTextMeaning = 
      <p>
      <b>Facing 3bet: </b> When you raise (the "2bet") and another player raises into you (the "3bet") and action folds back to you.
      </p>
    }
    else if (scenario == "Facing Raise First In") {
      scenarioTextMeaning = 
      <p>
      <b>Facing Raise First In: </b> When a player before you raises and action folds to you.
      </p>
    }
    
  return (
   
    <Container maxWidth="sm">
      <Grid container padding={1} borderBottom={"1px solid grey"}>
        <Grid size={4}>
          <Typography variant="h4"><b>Preflopify</b></Typography>
        </Grid>
        <Grid size={8}>
          <Typography align="right"><SimpleBackdrop text={infoText} buttonText={"Info"} icon={<InfoIcon/>}/></Typography>
        </Grid>
  
      </Grid>

      
      <Stack sx={{bgcolor:'secondary'}} padding={1} borderRadius="10px" margin={1}>
        {htmlParser.parse(rangeTable)}
      </Stack>
      <SimpleBackdrop text={"These charts assume a 6 max poker game with all players having at least 100 big blinds in their stack."} buttonText={"6 max 100BB eff."} icon={<HelpOutlineIcon/>}/>
      <SimpleBackdrop text={scenarioTextMeaning} buttonText={scenarioText} icon={<HelpOutlineIcon/>}/>
     
      <Typography variant="h5"><b>Dealt {hand} in {position}</b></Typography>
 
      <Stack spacing={1} direction="row" sx={{bgcolor:'dark', width:"100%"}} borderRadius="10px" padding={2} justifyContent={'center'}>
        {optionsList}
        <Button variant="outlined" onClick={() => reset()}><RestartAltIcon/></Button>
      </Stack>
      
    

    </Container>
     
      

   
  )
}

export default App
