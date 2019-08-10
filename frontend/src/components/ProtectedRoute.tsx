import * as React from 'react';
import {Route, RouteProps, Redirect} from 'react-router-dom';

interface IProtectedRoute extends RouteProps {
    authenticated: boolean;
    redirectPath: string;
}

export default class ProtectedRoute extends Route<IProtectedRoute> {
    public render() {
        const {authenticated, redirectPath} = this.props;
        if (authenticated && redirectPath) {
            return <Redirect to={redirectPath} />;
        }
        return <Route {...this.props}/>;
    }
}
