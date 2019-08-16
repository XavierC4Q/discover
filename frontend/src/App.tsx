import * as React from 'react';
import CssBaseline from '@material-ui/core/CssBaseline';
import Container from '@material-ui/core/Container';
import Content from './components/Content';
import Footer from './components/Footer';
import SearchAppBar from './components/SearchBar';

const App: React.FC = () => {
  return (
    <React.Fragment>
      <Container maxWidth={false}>
        <CssBaseline />
        <SearchAppBar />
        <Content />
        <Footer />
      </Container>
    </React.Fragment>
  );
};

export default App;
