import React from 'react';
import Box from '@material-ui/core/Box';
import Button from '@material-ui/core/Button';
import Container from '@material-ui/core/Container';
import gql from 'graphql-tag';
import TextField from '@material-ui/core/TextField';
import Typography from '@material-ui/core/Typography';
import {useFormStyles} from '../styles/formStyles';
import {useMutation} from '@apollo/react-hooks';

const SIGNUP_USER = gql`
  mutation signupUser($username: String!, $password: String!, $email: String!) {
    signup(username: $username, password: $password, email: $email) {
      newUser {
        id
        username
        email
        accountType
      }
    }
  }
`;

const GET_AUTH_TOKEN = gql`
  mutation getAuthToken($username: String!, $password: String!) {
    getToken(username: $username, password: $password) {
      token
      user {
        id
        email
        username
        dateJoined
        lastLogin
        accountType
      }
    }
  }
`;

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

  const [loginUser] = useMutation(GET_AUTH_TOKEN);

  const [signupUser] = useMutation(SIGNUP_USER, {
    variables: {
      username: inputs.username,
      password: inputs.password,
      email: inputs.email
    },
    update: async (cache, {data: {signup}}) => {
      const handleLogin = await loginUser({variables: {username: inputs.username, password: inputs.password}});
      if (handleLogin) {
        const {data: {getToken}} = handleLogin;
        localStorage.setItem('AUTH TOKEN', getToken.token);
        cache.writeData({
          data: {
            currentUser: {...getToken.user}
          }
        });
      }
    }
  });

  const handleInput = (name: keyof IState) => (e: React.ChangeEvent<HTMLInputElement>) =>
    setInputs({...inputs, [name]: e.target.value});

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    const {password, confirmPassword} = inputs;
    if (password === confirmPassword) {
      signupUser();
    }
  };

  return (
    <Container component="main" maxWidth="xs">
      <div className={classes.formContainer}>
        <Typography component="h1" variant="h5">
          Sign up
        </Typography>
        <form className={classes.form} noValidate onSubmit={handleSubmit}>
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
