import gql from 'graphql-tag';

const UserInputType = gql`
    type UserInput {
        id: Int!
        username: String!
        email: String!
        dateJoined: Int!
        lastLogin: Int
        latitude: Float!
        longitude: Float!
        searchDistance: Int!
        __typename: String!
    }
`;

export default [UserInputType];
