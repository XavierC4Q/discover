import {cache, apolloClient} from '../apolloClient';
import {ApolloCache} from 'apollo-cache';
import ApolloClient from 'apollo-client';

type TApolloCache = ApolloCache<typeof cache>;
type TApolloClient = ApolloClient<typeof apolloClient>;

enum ResolverKeys {
    MUTATION = 'Mutation',
    QUERY = 'Query',
    SUBSCRIPTION = 'Subscription'
}

type TResolverFunction = (
    parent: any,
    args: {[key: string]: any},
    {cache, client}: {cache: TApolloCache, client: TApolloClient},
    info: any
) => Promise<any> | any;

export interface IResolver {
    resolvers: {
        [ResolverKeys.QUERY]?: {
            [key: string]: TResolverFunction
        } | undefined,
        [ResolverKeys.MUTATION]?: {
            [key: string]: TResolverFunction
        } | undefined,
        [ResolverKeys.SUBSCRIPTION]?: {
            [key: string]: TResolverFunction
        } | undefined
    };
    defaults: {
        [key: string]: any
    };
}
