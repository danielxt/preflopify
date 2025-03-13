import * as React from 'react';
import Backdrop from '@mui/material/Backdrop';

import Button from '@mui/material/Button';
import { Box } from '@mui/material';
import Grid from '@mui/material/Grid2';

export default function SimpleBackdrop({text, buttonText, icon}) {
  const [open, setOpen] = React.useState(false);
  const handleClose = () => {
    setOpen(false);
  };
  const handleOpen = () => {
    setOpen(true);
  };

  return (
    <div>
      <Button variant="outlined" onClick={handleOpen} endIcon={icon} color="white"> {buttonText}</Button>

      <Backdrop
        sx={(theme) => ({ color: '#fff', zIndex: theme.zIndex.drawer + 1 })}
        open={open}
        onClick={handleClose}
        scro
      >
        <Grid container bgcolor={"white"} sx={{color:"black", width:"500px"}} borderRadius={"5px"} padding={1}>
          {text}
        </Grid>
      </Backdrop>
    </div>
  );
}
