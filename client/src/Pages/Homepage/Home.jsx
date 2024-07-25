import React, { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import axios from 'axios';

import Nav from '../../Components/Navbar/Nav';
import HeadImg from '../../Components/HeadImg/HeadImg';
import Content1 from '../../Components/Content1/Content1';
import Card from '../../Components/Card/Card';
import Header from '../../Components/Header/Header';
import Footer from '../../Components/Footer/Footer';
import WhyChoose from '../../Components/WhyChoose/WhyChoose';
import Customers from '../../Components/Customers/Customers';
import Services from '../../Components/Services/Services';

function Home() {

    return (<div>
                <Nav />
                <HeadImg />
                <Content1 />
                <WhyChoose />
                
                <Services />
                <Customers />
                <Footer />
            </div>)
}

export default Home;