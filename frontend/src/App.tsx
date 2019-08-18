import React from 'react';
import CssBaseline from '@material-ui/core/CssBaseline';
import Container from '@material-ui/core/Container';
import Content from './components/Content';
import Footer from './components/Footer';
import SearchBar from './components/SearchBar';
import gql from 'graphql-tag';
import {useQuery} from '@apollo/react-hooks';

const GET_CURRENT_USER = gql`
  query getCurrentUser {
    currentUser @client {
      id
    }
  }
`;

const App: React.FC = () => {
  const {data} = useQuery(GET_CURRENT_USER);
  return (
    <React.Fragment>
      <Container maxWidth={false}>
        <CssBaseline />
        <SearchBar currentUser={data.currentUser}/>
        <Content />
        <Footer />
      </Container>
    </React.Fragment>
  );
};

export default App;
