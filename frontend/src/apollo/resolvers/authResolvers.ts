import {IResolver} from '../../types/apollo';

const authResolver: IResolver = {
  resolvers: {
    Mutation: {
      logoutUser: (_, args, {cache}) => {
        localStorage.removeItem('AUTH TOKEN');
        cache.writeData({
          data: {
            currentUser: null
          }
        });
        return null;
      }
    }
  },
  defaults: {
    currentUser: null
  }
};

export default authResolver;
