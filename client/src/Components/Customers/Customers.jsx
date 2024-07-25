import React from 'react';
import "./Customers.css";

import tesla from '../../assets/tesla2.webp'
import facebook from '../../assets/facebook2.png'
import amazon from '../../assets/aws.png'
import spacex from '../../assets/spacex.png'
import openai from '../../assets/openai.png'
import netflix from '../../assets/netflix.png'
import google from '../../assets/google.png'

function Customers() {
    return(
            <div className='slide-body'>
                <h2>Our Clients</h2>
                <hr />
                <div className='slider'>
                    <div className='slide-track'>
                        <div className='slide'>
                            <img id="tesla" src={tesla}  alt="tesla" />
                        </div>
                        <div className='slide'>
                            <img id="facebook" src={facebook}  alt="facebook" />
                        </div>
                        <div className='slide'>
                            <img id="amazon" src={amazon}  alt="amazon" />
                        </div>
                        <div className='slide'>
                            <img id="spacex" src={spacex}  alt="spacex" />
                        </div>
                        <div className='slide'>
                            <img id="openai" src={openai}  alt="openai" />
                        </div>
                        <div className='slide'>
                            <img id="netflix" src={netflix}  alt="netflix" />
                        </div>
                        <div className='slide'>
                            <img id="google" src={google}  alt="google" />
                        </div>


                        <div className='slide'>
                            <img id="tesla" src={tesla}  alt="tesla" />
                        </div>
                        <div className='slide'>
                            <img id="facebook" src={facebook}  alt="facebook" />
                        </div>
                        <div className='slide'>
                            <img id="amazon" src={amazon}  alt="amazon" />
                        </div>
                        <div className='slide'>
                            <img id="spacex" src={spacex}  alt="spacex" />
                        </div>
                        <div className='slide'>
                            <img id="openai" src={openai}  alt="openai" />
                        </div>
                        <div className='slide'>
                            <img id="netflix" src={netflix}  alt="netflix" />
                        </div>
                        <div className='slide'>
                            <img id="google" src={google}  alt="google" />
                        </div>

                    </div>
                </div>
            </div>
            
        );
}

export default Customers;