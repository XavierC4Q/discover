import * as React from 'react';
import {Route} from 'react-router-dom';
import gql from 'graphql-tag';
import {useQuery} from '@apollo/react-hooks';
import Login from './Login';
import ProtectedRoute from './ProtectedRoute';

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
      <ProtectedRoute
        exact
        path="/auth/login"
        authenticated={data && data.currentUser}
        redirectPath="/"
        component={Login}
      />
    </React.Fragment>
  );
};

export default Content;
