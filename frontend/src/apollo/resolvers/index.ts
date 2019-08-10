import {merge} from 'lodash';
import authResolver from './authResolvers';

const {defaults, resolvers} = merge({}, authResolver);

export {defaults, resolvers};
