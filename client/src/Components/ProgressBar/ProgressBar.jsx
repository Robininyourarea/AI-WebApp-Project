import React from 'react';
import './ProgressBar.css';

function ProgressBar(props)  {
    return (
            <div className='progress-body'>
                <div className='prediction-container'>
                    <h3>Prediction</h3>
                    <div className='skill-box'>
                        <span className="title">{props.label1}</span>
                            
                        <div className='skill-bar'>
                            <span className='skill-per c1' style={{ width: `${props.value1 * 100}%` }}>
                                <span className='tooltip'>{(props.value1 * 100).toFixed(2)} %</span>
                            </span>
                        </div>
                    </div>

                    <div className='skill-box'>
                        <span className="title">{props.label2}</span>
                            
                        <div className='skill-bar'>
                            <span className='skill-per c2' style={{ width: `${props.value2 * 100}%` }}>
                                <span className='tooltip'>{(props.value2 * 100).toFixed(2)} %</span>
                            </span>
                        </div>
                    </div>

                    <div className='skill-box'>
                        <span className="title">{props.label3}</span>
                            
                        <div className='skill-bar'>
                            <span className='skill-per c3' style={{ width: `${props.value3 * 100}%` }}>
                                <span className='tooltip'>{(props.value3 * 100).toFixed(2)} %</span>
                            </span>
                        </div>
                    </div>

                    <div className='skill-box'>
                        <span className="title">{props.label4}</span>
                            
                        <div className='skill-bar'>
                            <span className='skill-per c4' style={{ width: `${props.value4 * 100}%` }}>
                                <span className='tooltip'>{(props.value4 * 100).toFixed(2)} %</span>
                            </span>
                        </div>
                    </div>
                    
                </div>
            </div>
        
    );
}

export default ProgressBar;

