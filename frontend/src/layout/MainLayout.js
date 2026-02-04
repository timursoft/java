import React from 'react';
import Header from '../components/Header';
import Footer from '../components/Footer';
import Navigation from '../components/Navigation';

function MainLayout() {
    return (
        <div>
            <Header />
            <Navigation />
            {/* Add Route components here */}
            <Footer />
        </div>
    );
}

export default MainLayout;
