import * as React from 'react';
import ReactDOM from 'react-dom';
import {BrowserRouter} from 'react-router-dom';
import {ApolloProvider} from 'react-apollo';
import {ApolloProvider as ApolloHooksProvider} from '@apollo/react-hooks';
import App from './App';
import {apolloClient} from './apolloClient';
import * as serviceWorker from './serviceWorker';

const ApolloApp = () => (
  <BrowserRouter>
    <ApolloProvider client={apolloClient}>
      <ApolloHooksProvider client={apolloClient}>
        <App />
      </ApolloHooksProvider>
    </ApolloProvider>
  </BrowserRouter>
);

ReactDOM.render(<ApolloApp />, document.getElementById('root'));

serviceWorker.unregister();
