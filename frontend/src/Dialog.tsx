import * as React from 'react';
import Button from '@mui/material/Button';
import Dialog, { DialogProps } from '@mui/material/Dialog';
import DialogActions from '@mui/material/DialogActions';
import DialogContent from '@mui/material/DialogContent';
import DialogContentText from '@mui/material/DialogContentText';
import DialogTitle from '@mui/material/DialogTitle';
import InfoIcon from '@mui/icons-material/Info';
import { Typography } from '@mui/material';

export default function ScrollDialog() {
  const [open, setOpen] = React.useState(false);
  const [scroll, setScroll] = React.useState<DialogProps['scroll']>('paper');

  const handleClickOpen = (scrollType: DialogProps['scroll']) => () => {
    setOpen(true);
    setScroll(scrollType);
  };

  const handleClose = () => {
    setOpen(false);
  };

  const descriptionElementRef = React.useRef<HTMLElement>(null);
  React.useEffect(() => {
    if (open) {
      const { current: descriptionElement } = descriptionElementRef;
      if (descriptionElement !== null) {
        descriptionElement.focus();
      }
    }
  }, [open]);

  return (
    <React.Fragment>
 
      <Button onClick={handleClickOpen('body')} color="white" endIcon={<InfoIcon/>} variant='outlined' >Need Help?</Button>
      <Dialog
        open={open}
        onClose={handleClose}
        scroll={scroll}
        aria-labelledby="scroll-dialog-title"
        aria-describedby="scroll-dialog-description"
      >
        <DialogContent dividers={scroll === 'paper'}>
          <DialogContentText
            id="scroll-dialog-description"
            ref={descriptionElementRef}
            tabIndex={-1}
            color="black"
          >
             <Typography variant="h5">
        <b>What is Preflopify?</b>
      </Typography>
      <Typography align="left">
        <p>
        Preflopify is a poker preflop range trainer designed to help you make better decisions on poker's first betting street. This tool allows players to efficiently practice hundreds of preflop spots within minutes, helping players of all skill levels develop a solid preflop strategy, the foundation for optimal play.
        </p>      
      </Typography>
      <Typography variant="h5">
        <b>How does Preflopify work?</b>
      </Typography>
      <Typography align="left">
        <p>
          Preflopify first chooses a random <b>hand</b>, table <b>position</b>, and <b>preflop scenario</b>. It then asks the player to choose the <a href="https://www.pokercode.com/blog/gto-poker">Game Theory Optimal (GTO)</a> action given these factors. After choosing an action, the optimal play is revealed and the table shows the full GTO chart for the position and scenario.
        </p>      
      </Typography>
 
      <Typography variant="h5">
        <b>What is a Hand?</b>
      </Typography>
      <Typography align="left">
        <p>
        A hand is the two cards received by the player before the flop. The table below simplifies all possible hands down to the 139 combos of pairs (e.g: AA), suited cards (e.g: AKs), and offsuit cards (e.g: AKo). 
        
        
        </p>
        <p><i>Tip: After choosing an action, try hovering over the colored cells to see the optimal action for that card.</i></p>
      </Typography>

      <Typography variant="h5">
        <b>What is Position?</b>
      </Typography>
      <Typography align="left">
        <p>
        Table position is the relative order of action of each player around the poker table. When playing, click on the Position button to see the table positions for a 6 max game.
        </p>
      </Typography>

      <Typography variant="h5">
        <b>What is a Scenario?</b>
      </Typography>
      <Typography align="left">
        <p>
        Preflopify supports three common preflop scenarios players may face: <b>Raising First In</b>, <b>Facing Raise First In</b>, and <b>Facing 3bet</b>. When playing, click on the Scenario button to see a description of the current scenario.
        </p>
      </Typography>

      <Typography variant="h5">
        <b>Why don't I have the option to call/limp in certain spots?</b>
      </Typography>
      <Typography align="left">
        <p>
            Particularly in the small blind, GTO recommends a pure 3 bet / fold strategy, meaning that a player should never call/limp in these spots or they would be playing suboptimally.
        </p>
      </Typography>

      <Typography variant="h5">
        <b>What preflop charts are used?</b>
      </Typography>
      <Typography align="left">
        <p>
            Preflop charts taken from <a href="https://github.com/fordbjay/poker-preflop-charts/blob/ef0e24e41fac6b0ede50569faf504e4b36aaaa98/src/components/chart.vue#L62C1-L62C1">@fordbjay's poker-preflop-charts</a> repository. 
        </p>
      </Typography>
          </DialogContentText>
        </DialogContent>
        <DialogActions>
          <Button onClick={handleClose}>Close</Button>
        </DialogActions>
      </Dialog>
    </React.Fragment>
  );
}