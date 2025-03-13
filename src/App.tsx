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
import SettingsIcon from '@mui/icons-material/Settings';

import ScrollDialog from './Dialog.tsx'
import pokerPositions from './assets/pokerPositions.png'
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

    var endpoint = ""
    if (import.meta.env.MODE == "development") {
      endpoint = import.meta.env.VITE_DEV_API_ENDPOINT
      
    }
    else {
      endpoint = import.meta.env.VITE_PROD_API_ENDPOINT
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
      const response = await fetch(endpoint)
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

    var positionTextMeaning = (
          <>
           <img src={pokerPositions} width="100%"/>
           <Typography textAlign={"left"}>
            In preflop (for a 6 max game), from first to play to last is:
            <p>
            1.<b> LJ / Lojack</b> (also known as UTG / Under the Gun)
            </p>
            <p>
            2.<b> HJ / Hijack</b> (also known as UTG+1)
            </p>
            <p>
            3.<b> CO / Cutoff</b>
            </p>
            <p>
            4.<b> BTN / Button</b>
            </p>
            <p>
            5.<b> SB / Small Blind</b>
            </p>
            <p>
            6.<b> BB / Big Blind</b>
            </p>
           </Typography>
          </>
          

     
    )

    var settingsText = (
      <>
      <p> Coming soon... </p>
      </>
      
    )
  return (
   
    <Container maxWidth="sm">
      <Grid container padding={1} borderBottom={"1px solid grey"}>
        <Grid size={4}>
          <Typography variant="h4"><b>Preflopify</b></Typography>
        </Grid>

        <Grid size={8}>
        <Typography align="right"><SimpleBackdrop text={settingsText} buttonText={"Settings"}icon={<SettingsIcon/>}/></Typography>
        </Grid>
   
  
      </Grid>


      <Typography align="center" padding={1}><ScrollDialog/></Typography>
  
      <Stack sx={{bgcolor:'secondary'}} padding={1} borderRadius="10px" margin={1} spacing={2}>
        {htmlParser.parse(rangeTable)}
        <SimpleBackdrop text={"These charts assume a 6 max poker game with all players having at least 100 big blinds in their stack."} buttonText={"6 max 100BB eff."} icon={<HelpOutlineIcon/>}/>
        
        <Stack direction="row" spacing={2} justifyContent={"center"}>
        <SimpleBackdrop text={scenarioTextMeaning} buttonText={scenarioText} icon={<HelpOutlineIcon/>}/>
        <SimpleBackdrop text={positionTextMeaning} buttonText={"Position"} icon={<HelpOutlineIcon/>}/>
        </Stack>
        
      </Stack>

  

      <Typography variant="h5"><b>Dealt {hand} in {position}</b></Typography>
 
      <Stack spacing={1} direction="row" sx={{bgcolor:'dark', width:"100%"}} borderRadius="10px" padding={2} justifyContent={'center'}>
        {optionsList}
        <Button variant="outlined" onClick={() => reset()}><RestartAltIcon/></Button>
      
      </Stack>
      
    

    </Container>
     
      

   
  )
}

export default App
