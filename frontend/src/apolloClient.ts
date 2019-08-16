import {ApolloClient} from 'apollo-client';
import {InMemoryCache} from 'apollo-cache-inmemory';
import {withClientState} from 'apollo-link-state';
import {ApolloLink} from 'apollo-link';
import {HttpLink} from 'apollo-link-http';
import {setContext} from 'apollo-link-context';
import {defaults, resolvers} from './apollo/resolvers/index';
import typeDefs from './apollo/typeDefs/index';

const AUTH_TOKEN = localStorage.getItem('AUTH TOKEN');

export const cache = new InMemoryCache();

const authLink = setContext(() => ({
  headers: {
    Authorization: AUTH_TOKEN ? `Bearer ${AUTH_TOKEN}` : ''
  }
}));

const httpLink = new HttpLink({
  uri: 'http://127.0.0.1:8000/graphql'
});

const stateLink = withClientState({
  cache,
  resolvers,
  defaults,
  typeDefs
});

const link = ApolloLink.from([stateLink, authLink, httpLink]);

export const apolloClient = new ApolloClient({
  link,
  cache,
  resolvers: resolvers as any,
  typeDefs
});
