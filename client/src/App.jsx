import React, {useEffect, useState} from 'react';
import {BrowserRouter, Routes, Route} from 'react-router-dom'
import axios from 'axios';

import Nav from './Components/Navbar/Nav.jsx'
import Card from './Components/Card/Card.jsx'
import Header from './Components/Header/Header.jsx';
import Footer from './Components/Footer/Footer.jsx';

import Home from './Pages/Homepage/Home.jsx';
import Login from './Pages/Login/Login.jsx';
import Register from './Pages/Register/Register.jsx';
import Models from './Pages/Models/Models.jsx';
import About from './Pages/About/About.jsx';
import Contact from './Pages/Contact/Contact.jsx';

import Object from './Pages/Object/Object.jsx';
import Classify from './Pages/Clssify/Classify.jsx';
import Segment from './Pages/Segment/Segment.jsx';

function App() {

  return (<div>
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Login />}></Route>
        <Route path="/register" element={<Register />}></Route>
        <Route path="/home" element={<Home />}></Route>
        <Route path="/models" element={<Models />}></Route>
        <Route path="/about" element={<About />}></Route>
        <Route path="/contact" element={<Contact />}></Route>
        <Route path="/object" element={<Object />}></Route>
        <Route path="/classify" element={<Classify />}></Route>
        <Route path="/segment" element={<Segment />}></Route>
      </Routes>
    </BrowserRouter>
</div>)
}


export default App;
