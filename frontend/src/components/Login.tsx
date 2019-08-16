import * as React from 'react';
import gql from 'graphql-tag';
import {useMutation} from '@apollo/react-hooks';
import TextField from '@material-ui/core/TextField';
import Button from '@material-ui/core/Button';
import Card from '@material-ui/core/Card';
import Title from './Title';

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

const Login = () => {
  const [inputs, setInputs] = React.useState({
    username: '',
    password: ''
  });
  const [getAuthToken, {error, loading}] = useMutation(GET_AUTH_TOKEN, {
    variables: {
      username: inputs.username,
      password: inputs.password
    },
    update: (cache, {data}) => {
      if (data && data.getToken) {
        const {token, user} = data.getToken;
        localStorage.setItem('AUTH TOKEN', token);
        cache.writeData({
          data: {
            currentUser: {...user}
          }
        });
        return null;
      }
    }
  });

  const handleInput = (name: string) => (e: React.ChangeEvent<HTMLInputElement>) =>
    setInputs({...inputs, [name]: e.target.value});

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    await getAuthToken();
  };
  return (
    <Card raised={false} className="flex-column form-card">
      <Title>Login Here</Title>
      <form noValidate autoComplete="off" autoSave="off" onSubmit={handleSubmit}>
        <TextField
          id="username"
          label="Enter Username"
          required
          value={inputs.username}
          onChange={handleInput('username')}
          margin="normal"
        />
        <TextField
          id="password"
          label="Enter Password"
          required
          value={inputs.password}
          onChange={handleInput('password')}
          margin="normal"
        />
        <Button color="primary" size="medium" type="submit">
          Submit
        </Button>
      </form>
    </Card>
  );
};

export default Login;
