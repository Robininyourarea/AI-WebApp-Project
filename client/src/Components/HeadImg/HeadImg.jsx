import React from 'react';
import "./HeadImg.css";

function HeadImg() {
    return(
        <div className="head-img-container">
            <div className="navbar-placeholder"></div>
            <div className="contents">
                <h1>TRANSFORMING THE FUTURE WITH AI</h1>
                <p>We revolutionize industries with cutting-edge AI solutions, driving efficiency and unlocking new possibilities for businesses worldwide.</p>
                <button className="cta-button">SEE OUR PROJECTS</button>
            </div>
        </div>
        );
}

export default HeadImg;