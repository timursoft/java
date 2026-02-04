import React from 'react';
import { BrowserRouter as Router } from 'react-router-dom';
import MainLayout from './layout/MainLayout';
import './styles/global.css';

function App() {
    return (
        <Router>
            <MainLayout />
        </Router>
    );
}

export default App;
