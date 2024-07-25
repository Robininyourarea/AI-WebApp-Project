import React, {useState} from 'react';
import { useNavigate } from 'react-router-dom';
import "./Card.css";
import classify from '../../assets/class.png'
import segment from '../../assets/segment.jpeg'
import object from '../../assets/object.jpeg'

function Card() {
    const navigateTo = useNavigate();

    const objectPage = () => {
        navigateTo("/object");
    };

    const classifyPage = () => {
        navigateTo("/classify");
    };

    const segmentPage = () => {
        navigateTo("/segment");
    };
    
    return(
            <div>
                <section className='cards'>
                
                    <div className='card'>

                        <div>
                            <img className="card-img" src={classify} alt="" />
                        </div>

                        <div>
                            <h3>Classification</h3>
                            <p>EfficientNet is a state-of-the-art model for image classification that achieves superior accuracy with fewer parameters, making it highly efficient for real-world applications.</p>
                        </div>

                        <div>
                        <button className="card-button" onClick={classifyPage}>Let's Try</button>
                        </div>
                    </div>

                    <div className='card'>

                        <div>
                            <img className="card-img" src={segment} alt="" />
                        </div>

                        <div>
                            <h3>Segmentation</h3>
                            <p>U-NET is a powerful deep learning model for image segmentation, enabling precise delineation of objects in images, widely used in medical imaging and other fields.</p>
                        </div>

                        <div>
                            <button className="card-button" onClick={segmentPage}>Let's Try</button>
                        </div>
                    </div>

                    <div className='card'>

                        <div>
                            <img className="card-img" src={object} alt="" />
                        </div>

                        <div>
                            <h3>Object Detection</h3>
                            <p>YOLOv8 is a cutting-edge model for real-time object detection, offering high speed and accuracy for identifying and locating objects in images and videos.</p>
                        </div>

                        <div>
                        <button className="card-button" onClick={objectPage}>Let's Try</button>
                        </div>
                    </div>
                </section>
            </div>
        )
}

export default Card;