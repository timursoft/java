import React from 'react';
import PropTypes from 'prop-types';
import { NavBar } from '../Header/NavBar';
import '../../styles/global.css';

const MainLayout = ({ children }) => {
    return (
        <div className="main-layout">
            <NavBar />
            <div className="content">
                {children}
            </div>
        </div>
    );
};

MainLayout.propTypes = {
    children: PropTypes.node.isRequired,
};

export default MainLayout;
