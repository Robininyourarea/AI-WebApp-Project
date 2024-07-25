import React, { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';

import Nav from '../../Components/Navbar/Nav';

import Card from '../../Components/Card/Card';

import Footer from '../../Components/Footer/Footer';


import "./Models.css";
import classify from '../../assets/class.png'
import segment from '../../assets/segment.jpeg'
import object from '../../assets/object.jpeg'
import llm from '../../assets/LLM1.jpg'
import midj from '../../assets/midj2.png'
import anom from '../../assets/anom.jpg'
function Models() {
    const navigateTo = useNavigate();

    const cardsData = [
        {
            imgSrc: classify, 
            title: 'Classification',
            description: 'EfficientNet is a state-of-the-art model for image classification that achieves superior accuracy with fewer parameters, making it highly efficient for real-world applications.',
            onClickFn: () => navigateTo("/classify") 
        },
        {
            imgSrc: segment, 
            title: 'Segmentation',
            description: 'U-NET is a powerful deep learning model for image segmentation, enabling precise delineation of objects in images, widely used in medical imaging and other fields.',
            onClickFn: () => navigateTo("/segment") 
        },
        {
            imgSrc: object, 
            title: 'Object Detection',
            description: 'YOLOv8 is a cutting-edge model for real-time object detection, offering high speed and accuracy for identifying and locating objects in images and videos.',
            onClickFn: () => navigateTo("/object") 
        },
        {
            imgSrc: midj, 
            title: 'Image Generation',
            description: 'GPT-4 is a powerful language model capable of generating coherent and contextually relevant text, revolutionizing natural language understanding and generation tasks.',
            
        },
        {
            imgSrc: anom, 
            title: 'Anomaly Detection',
            description: 'STM-based models are used for time series anomaly detection, identifying unusual patterns in data that do not conform to expected behavior.',
            
        },
        {
            imgSrc: llm, 
            title: 'Large Language Model',
            description: 'GPT-4, is a state-of-the-art AI model designed to process and generate human-like text leverages deep learning techniques to understand and generate relevant language',
           
        }
    ];

    return (<div>
                <Nav />
                <div className='our-model-header'>
                    <h2>Our Models</h2>
                    <p>This AI model is a demo for testing purposes.</p>
                </div>
                <div className='model-cards'>
                    {cardsData.map((card, index) => (
                        <Card 
                            key={index} 
                            imgSrc={card.imgSrc}
                            title={card.title}
                            desc={card.description}
                            onClick={card.onClickFn} />
                    ))}
                </div>
                <Footer />
            </div>)
}

export default Models;