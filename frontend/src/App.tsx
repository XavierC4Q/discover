import * as React from 'react';
import CssBaseline from '@material-ui/core/CssBaseline';
import Container from '@material-ui/core/Container';
import Content from './components/Content';
import Footer from './components/Footer';
import SearchAppBar from './components/SearchBar';
import './styles/App.css';

const App: React.FC = () => {
  return (
    <React.Fragment>
      <CssBaseline />
      <SearchAppBar />
      <Container maxWidth={false} className="App">
        <Content />
        <Footer />
      </Container>
    </React.Fragment>
  );
};

export default App;
