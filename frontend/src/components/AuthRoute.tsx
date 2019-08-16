import * as React from 'react';
import {Route, RouteProps, Redirect} from 'react-router-dom';

interface IAuthRoute extends RouteProps {
    authenticated: boolean;
}

export default class AuthRoute extends Route<IAuthRoute> {
    public render() {
        const {authenticated} = this.props;
        if (authenticated) {
            return <Redirect to='/' />;
        }
        return <Route {...this.props}/>;
    }
}