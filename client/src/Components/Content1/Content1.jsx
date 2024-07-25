import React from 'react';
import './Content1.css';
import aiImage from '../../assets/Robot.png'; 
import robot from '../../assets/cute-robot.avif';
function Content1() {
    return (
        <div className="content1-container">
            <div className="content1-left">
                <img src={aiImage} alt="Cleaning Service" className="content1-img"/>
            </div>
            <div className="content1-right">
                <h3>COMPANY MISSION</h3>
                <h1>Innovative AI Solutions for a Smarter Future</h1>
                <p>
                        At NeuralTech, our mission is to harness the power of artificial intelligence to drive innovation and create smarter solutions for businesses and individuals. 
                    Our cutting-edge AI technologies are designed to solve complex problems, enhance productivity, and unlock new opportunities across various industries.
                    We are committed to making AI accessible and beneficial to all, paving the way for a brighter and more efficient future.
                </p>
                <button className="learn-more-btn">LEARN MORE</button>
            </div>
        </div>
    );
}

export default Content1;