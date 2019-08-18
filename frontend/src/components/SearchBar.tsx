import React from 'react';
import AppBar from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar';
import Typography from '@material-ui/core/Typography';
import {IUser} from '../types/users';
import {useSearchBarStyles} from '../styles/searchBarStyles';
import Title from './Title';

interface IProps {
  currentUser: null | IUser;
}

const SearchBar: React.FC<IProps> = ({currentUser}) => {
  const classes = useSearchBarStyles();

  return (
    <div className={classes.root}>
      <AppBar position="static" color="primary">
        <Toolbar>
          <Title>Discover</Title>
        </Toolbar>
      </AppBar>
    </div>
  );
};

export default SearchBar;
