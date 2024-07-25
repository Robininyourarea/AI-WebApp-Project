import React, {useState} from 'react';
import "./Card.css";

function Card(props) {

    
    return(
            <div>
                <section className='cards'>
                
                    <div className='card'>

                        <div>
                            <img className="card-img" src={props.imgSrc} alt="" />
                        </div>

                        <div>
                            <h3>{props.title}</h3>
                            <p>{props.desc}</p>
                        </div>

                        <div>
                        <button className="card-button" onClick={props.onClick}>Let's Try</button>
                        </div>
                    </div>

                    
                </section>
            </div>
        )
}

export default Card;