import * as React from 'react';
import Button from '@material-ui/core/Button';
import TextField from '@material-ui/core/TextField';
import Box from '@material-ui/core/Box';
import Typography from '@material-ui/core/Typography';
import {useFormStyles} from '../styles/formStyles';
import Container from '@material-ui/core/Container';

interface IState {
  username: string;
  email: string;
  password: string;
  confirmPassword: string;
}

const SignUp: React.FC = () => {
  const classes = useFormStyles();
  const [inputs, setInputs] = React.useState<IState>({
    username: '',
    password: '',
    confirmPassword: '',
    email: ''
  });

  const handleInput = (name: keyof IState) => (e: React.ChangeEvent<HTMLInputElement>) =>
    setInputs({...inputs, [name]: e.target.value});

  return (
    <Container component="main" maxWidth="xs">
      <div className={classes.formContainer}>
        <Typography component="h1" variant="h5">
          Sign up
        </Typography>
        <form className={classes.form} noValidate>
          <TextField
            id="username"
            label="Enter Your Username"
            value={inputs.username}
            required
            fullWidth
            margin="normal"
            onChange={handleInput('username')}
          />
          <TextField
            id="email"
            label="Enter Your Email"
            value={inputs.email}
            required
            fullWidth
            margin="normal"
            onChange={handleInput('email')}
          />
          <TextField
            id="password"
            label="Enter Your Password"
            value={inputs.password}
            required
            fullWidth
            margin="normal"
            onChange={handleInput('password')}
          />
          <TextField
            id="confirmPassword"
            label="Confirm Your Password"
            value={inputs.confirmPassword}
            required
            fullWidth
            margin="normal"
            onChange={handleInput('confirmPassword')}
          />
          <Button type="submit" fullWidth variant="contained" color="primary" className={classes.submit}>
            Sign Up
          </Button>
        </form>
      </div>
      <Box mt={5} />
    </Container>
  );
};

export default SignUp;
