import React, { useEffect, useState } from 'react';


import elon from '../../assets/elon.jfif'
import jobs from '../../assets/jobs.webp'
import mark from '../../assets/mark.webp'
import sam from '../../assets/sam.webp'
import sunder from '../../assets/sunder.jpg'
import satya from '../../assets/satya.jfif'
import jeff from '../../assets/jeff.jpg'
import shou from '../../assets/shou.avif'

import "./Employee.css";

function Employee() {
    const [activeId, setActiveId] = useState('content1');

    const handleImgBxClick = (id) => {
        setActiveId(id);
    }

    return (<div>
                
                <div className='about-body'>
                    <div className='container'>
                        <div className='icon'>
                            <div className={`imgBx ${activeId === 'content1' ? 'active' : ''}`} style={{ '--i': 1 }} data-id="content1" onClick={() => handleImgBxClick('content1')}>
                                <img src={elon}/>
                            </div>
                            <div className={`imgBx ${activeId === 'content2' ? 'active' : ''}`} style={{ '--i': 2 }} data-id="content2" onClick={() => handleImgBxClick('content2')}>
                                <img src={jobs}/>
                            </div>
                            <div className={`imgBx ${activeId === 'content3' ? 'active' : ''}`} style={{ '--i': 3 }} data-id="content3" onClick={() => handleImgBxClick('content3')}>
                                <img src={mark}/>
                            </div>
                            <div className={`imgBx ${activeId === 'content4' ? 'active' : ''}`} style={{ '--i': 4 }} data-id="content4" onClick={() => handleImgBxClick('content4')}>
                                <img src={sam}/>
                            </div>
                            <div className={`imgBx ${activeId === 'content5' ? 'active' : ''}`} style={{ '--i': 5 }} data-id="content5" onClick={() => handleImgBxClick('content5')}>
                                <img src={sunder}/>
                            </div>
                            <div className={`imgBx ${activeId === 'content6' ? 'active' : ''}`} style={{ '--i': 6 }} data-id="content6" onClick={() => handleImgBxClick('content6')}>
                                <img src={satya}/>
                            </div>
                            <div className={`imgBx ${activeId === 'content7' ? 'active' : ''}`} style={{ '--i': 7 }} data-id="content7" onClick={() => handleImgBxClick('content7')}>
                                <img src={jeff}/>
                            </div>
                            <div className={`imgBx ${activeId === 'content8' ? 'active' : ''}`} style={{ '--i': 8 }} data-id="content8" onClick={() => handleImgBxClick('content8')}>
                                <img src={shou}/>
                            </div>
                        </div>

                        <div className='content'>
                            <div className={`contentBx ${activeId === 'content1' ? 'active' : ''}`} id='content1'>
                                <div className='employee-card'>
                                    <div className='imgBx'>
                                        <img src={elon}/>
                                    </div>
                                    <div className='textBx'>
                                        <h2>Elon Musk<br /><span>Chief Executive Officer (CEO)</span></h2>
                                        <ul className='sci'>
                                            <li><a href="#"><i className='fab fa-facebook-f'></i></a></li>
                                            <li><a href="#"><i className='fab fa-twitter'></i></a></li>
                                            <li><a href="#"><i className='fab fa-instagram'></i></a></li>
                                            <li><a href="#"><i className='fab fa-linkedin-in'></i></a></li>
                                        </ul>
                                    </div>
                                </div>
                            </div>
                            <div className={`contentBx ${activeId === 'content2' ? 'active' : ''}`} id='content2'>
                                <div className='employee-card'>
                                    <div className='imgBx'>
                                        <img src={jobs}/>
                                    </div>
                                    <div className='textBx'>
                                        <h2>Steve Jobs<br /><span>Chief Product Officer (CPO)</span></h2>
                                        <ul className='sci'>
                                            <li><a href="#"><i className='fab fa-facebook-f'></i></a></li>
                                            <li><a href="#"><i className='fab fa-twitter'></i></a></li>
                                            <li><a href="#"><i className='fab fa-instagram'></i></a></li>
                                            <li><a href="#"><i className='fab fa-linkedin-in'></i></a></li>
                                        </ul>
                                    </div>
                                </div>
                            </div>
                            <div className={`contentBx ${activeId === 'content3' ? 'active' : ''}`} id='content3'>
                                <div className='employee-card'>
                                    <div className='imgBx'>
                                        <img src={mark}/>
                                    </div>
                                    <div className='textBx'>
                                        <h2>Mark Zuckerberg<br /><span>Chief Technology Officer (CTO)</span></h2>
                                        <ul className='sci'>
                                            <li><a href="#"><i className='fab fa-facebook-f'></i></a></li>
                                            <li><a href="#"><i className='fab fa-twitter'></i></a></li>
                                            <li><a href="#"><i className='fab fa-instagram'></i></a></li>
                                            <li><a href="#"><i className='fab fa-linkedin-in'></i></a></li>
                                        </ul>
                                    </div>
                                </div>
                            </div>
                            <div className={`contentBx ${activeId === 'content4' ? 'active' : ''}`} id='content4'>
                                <div className='employee-card'>
                                    <div className='imgBx'>
                                        <img src={sam}/>
                                    </div>
                                    <div className='textBx'>
                                        <h2>Sam Altman<br /><span>Director of AI</span></h2>
                                        <ul className='sci'>
                                            <li><a href="#"><i className='fab fa-facebook-f'></i></a></li>
                                            <li><a href="#"><i className='fab fa-twitter'></i></a></li>
                                            <li><a href="#"><i className='fab fa-instagram'></i></a></li>
                                            <li><a href="#"><i className='fab fa-linkedin-in'></i></a></li>
                                        </ul>
                                    </div>
                                </div>
                            </div>
                            <div className={`contentBx ${activeId === 'content5' ? 'active' : ''}`} id='content5'>
                                <div className='employee-card'>
                                    <div className='imgBx'>
                                        <img src={sunder}/>
                                    </div>
                                    <div className='textBx'>
                                        <h2>Sunder Pichai<br /><span>Chief Marketing Officer (CMO)</span></h2>
                                        <ul className='sci'>
                                            <li><a href="#"><i className='fab fa-facebook-f'></i></a></li>
                                            <li><a href="#"><i className='fab fa-twitter'></i></a></li>
                                            <li><a href="#"><i className='fab fa-instagram'></i></a></li>
                                            <li><a href="#"><i className='fab fa-linkedin-in'></i></a></li>
                                        </ul>
                                    </div>
                                </div>
                            </div>
                            <div className={`contentBx ${activeId === 'content6' ? 'active' : ''}`} id='content6'>
                                <div className='employee-card'>
                                    <div className='imgBx'>
                                        <img src={satya}/>
                                    </div>
                                    <div className='textBx'>
                                        <h2>Satya Nadella<br /><span>Chief Marketing Officer (CMO)</span></h2>
                                        <ul className='sci'>
                                            <li><a href="#"><i className='fab fa-facebook-f'></i></a></li>
                                            <li><a href="#"><i className='fab fa-twitter'></i></a></li>
                                            <li><a href="#"><i className='fab fa-instagram'></i></a></li>
                                            <li><a href="#"><i className='fab fa-linkedin-in'></i></a></li>
                                        </ul>
                                    </div>
                                </div>
                            </div>
                            <div className={`contentBx ${activeId === 'content7' ? 'active' : ''}`} id='content7'>
                                <div className='employee-card'>
                                    <div className='imgBx'>
                                        <img src={jeff}/>
                                    </div>
                                    <div className='textBx'>
                                        <h2>Jeff Bezos<br /><span>Chief Financial Officer (CFO) </span></h2>
                                        <ul className='sci'>
                                            <li><a href="#"><i className='fab fa-facebook-f'></i></a></li>
                                            <li><a href="#"><i className='fab fa-twitter'></i></a></li>
                                            <li><a href="#"><i className='fab fa-instagram'></i></a></li>
                                            <li><a href="#"><i className='fab fa-linkedin-in'></i></a></li>
                                        </ul>
                                    </div>
                                </div>
                            </div>
                            <div className={`contentBx ${activeId === 'content8' ? 'active' : ''}`} id='content8'>
                                <div className='employee-card'>
                                    <div className='imgBx'>
                                        <img src={shou}/>
                                    </div>
                                    <div className='textBx'>
                                        <h2>Shou Zi Chew<br /><span>Chief Information Officer (CIO)</span></h2>
                                        <ul className='sci'>
                                            <li><a href="#"><i className='fab fa-facebook-f'></i></a></li>
                                            <li><a href="#"><i className='fab fa-twitter'></i></a></li>
                                            <li><a href="#"><i className='fab fa-instagram'></i></a></li>
                                            <li><a href="#"><i className='fab fa-linkedin-in'></i></a></li>
                                        </ul>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                
            </div>)
}

export default Employee;