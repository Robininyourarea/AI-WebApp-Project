import React, { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import axios from 'axios';

import Nav from '../../Components/Navbar/Nav';
import HeadImg from '../../Components/HeadImg/HeadImg';
import Content1 from '../../Components/Content1/Content1';
import Card from '../../Components/Card/Card';
import Header from '../../Components/Header/Header';
import Footer from '../../Components/Footer/Footer';
import Employee from '../../Components/Employee/Employee';

import elon from '../../assets/elon.jfif'
import jobs from '../../assets/jobs.webp'
import mark from '../../assets/mark.webp'
import sam from '../../assets/sam.webp'
import sunder from '../../assets/sunder.jpg'
import satya from '../../assets/satya.jfif'
import jeff from '../../assets/jeff.jpg'
import shou from '../../assets/shou.avif'

import img1 from '../../assets/ai1.jpg'
import img2 from '../../assets/office2.webp'

import "./About.css";

function About() {
    const [activeId, setActiveId] = useState('content1');

    const handleImgBxClick = (id) => {
        setActiveId(id);
    }

    return (<div>
                <Nav />
                <div className='section-1'>
                    <h2>About NeuralTech</h2>
                </div>
                <div className='section-2'>
                    <h2>NeuralTech</h2>
                    <hr />
                    <p>Established in 2022, NeuralTech is a leading technology company specializing in end-to-end AI solutions. s<br /> This dynamic firm is dedicated to advancing the field of artificial intelligence, providing innovative<br /> and comprehensive AI services that drive digital transformation and support the day-to-day operations of businesses worldwide.</p>
                </div>
                <div className='section-3'>
                    <div className='sec-3-left'>
                        <img src={img1} />
                    </div>
                    <div className='sec-3-right'>
                        <h2>From AI development to seamless integration</h2>
                        <p>NeuralTech oversees a diverse portfolio of projects. Our achievements include NeuralAssist, a cutting-edge AI-powered platform that serves numerous clients globally and is continuously expanding its capabilities.</p>
                        <br />
                        <p>Apart from delivering end-to-end AI solutions, our innovation lab constantly generates new research and breakthrough ideas. We both develop our own solutions and collaborate with partners to create the AI-driven innovations their businesses and customers need. To maximize operational efficiency, each team at NeuralTech focuses on different specialties, from infrastructure, design, software development, operations, cybersecurity, and innovation.</p>
                        <br />
                        <p>We dedicate significant resources to data science, machine learning, and deep tech research in areas such as blockchain, facial recognition, NLP, quantum computing, and beyond, striving to uncover and harness new possibilities.</p>
                    </div>
                </div>
                <div className='section-4'>
                    <div className='sec-4-left'>
                    <h2>Transformation to increase our capability</h2>
                        <p>As NeuralTech expands into the global market, we are accelerating transformation to increase our capability and support our shared goal of international growth. After establishing TechHub, a state-of-the-art technology center in Silicon Valley, we are now setting up another office in Singapore called NeuralTech Asia to facilitate our overseas operations.</p>
                        <br />
                        <p>As we advance into the new era, NeuralTech’s ventures are also extending into the Metaverse: NeuroCube, our AI-driven virtual platform, and NeuralX, an innovation hub building trust in the world of AI and beyond. Scaling and growing faster than ever, NeuralTech strives to become the best AI technology company globally by 2025.</p>
                        <br />
                    
                    </div>
                    <div className='sec-4-right'>
                    <img src={img2} />
                    </div>
                </div>

                <div className='section-5'>
                    <div className='sec-5-left'>
                        <Employee />
                    </div>
                    <div className='sec-5-right'>
                        <h2>Our Teams</h2>
                        <hr />
                        <p>At NeuralTech, our team is our greatest asset. Comprised of top-tier AI experts, data scientists, software engineers, and industry specialists, we bring together a diverse array of skills and expertise to deliver cutting-edge AI solutions. Our team members are passionate about innovation and committed to excellence, continuously pushing the boundaries of technology to create impactful and transformative solutions for our clients.</p>
                        <br />
                        <p>Our collaborative culture fosters creativity and encourages continuous learning, enabling us to stay at the forefront of technological advancements. Each team member at NeuralTech plays a crucial role in our mission to revolutionize the AI landscape and deliver exceptional value to our partners and clients worldwide.</p>
                        <br />
                        <p>From developing sophisticated machine learning models to implementing advanced AI-driven applications, our team’s dedication and expertise ensure that NeuralTech remains a leader in the tech industry. We are proud to have a team that not only meets the challenges of today but also anticipates the opportunities of tomorrow.</p>
                    </div>
                </div>
                <Footer />
            </div>)
}

export default About;