import * as React from 'react';
import Backdrop from '@mui/material/Backdrop';

import Button from '@mui/material/Button';
import InfoIcon from '@mui/icons-material/Info';
import { Box } from '@mui/material';

export default function SimpleBackdrop() {
  const [open, setOpen] = React.useState(false);
  const handleClose = () => {
    setOpen(false);
  };
  const handleOpen = () => {
    setOpen(true);
  };

  return (
    <div>
      <Button variant="text" onClick={handleOpen}><InfoIcon/></Button>

      <Backdrop
        sx={(theme) => ({ color: '#fff', zIndex: theme.zIndex.drawer + 1 })}
        open={open}
        onClick={handleClose}
      >
        <Box>
          Some info!
        </Box>
      </Backdrop>
    </div>
  );
}
