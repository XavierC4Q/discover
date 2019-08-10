import * as React from 'react';
import Container from '@material-ui/core/Container';
import Content from './components/Content';
import Footer from './components/Footer';
import './styles/App.css';

const App: React.FC = () => {
  return (
    <Container maxWidth={false} className="App">
      <Content />
      <Footer />
    </Container>
  );
};

export default App;
