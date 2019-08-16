import * as React from 'react';
import AuthRoute from './AuthRoute';
import gql from 'graphql-tag';
import Login from './Login';
import ProtectedRoute from './ProtectedRoute';
import SignUp from './SignUp';
import { Route } from 'react-router-dom';
import { useQuery } from '@apollo/react-hooks';

const GET_CURRENT_USER = gql`
  query getCurrentUser {
    currentUser @client {
      id
    }
  }
`;

const Content = () => {
  const {data} = useQuery(GET_CURRENT_USER);
  return (
    <React.Fragment>
      <Route path='/' render={() => (<div>Home</div>)} />
      <AuthRoute
        exact
        path="/auth/login"
        authenticated={data && data.currentUser}
        component={Login}
      />
      <AuthRoute
        exact
        path="/auth/signup"
        authenticated={data && data.currentUser}
        component={SignUp}
      />
    </React.Fragment>
  );
};

export default Content;
