import React from 'react';
import { Link } from 'react-router-dom';
import '../../styles/global.css';

const NavBar = () => {
    return (
        <nav className="nav-bar">
            <ul className="nav-list">
                <li><Link to="/home">Home</Link></li>
                <li><Link to="/about">About</Link></li>
                <li><Link to="/contact">Contact</Link></li>
            </ul>
        </nav>
    );
};

export default NavBar;
