import * as React from 'react';
import Typography from '@material-ui/core/Typography';

const Title: React.FC<{children: React.ReactNode}> = (props) => (
  <Typography component="h1" variant="h5" color="textPrimary" gutterBottom>
    {props.children}
  </Typography>
);

export default Title;
