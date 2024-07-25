import React, { useState, useEffect } from 'react';
import './WhyChoose.css';
import logo_ai from '../../assets/ai.png';
import eff from '../../assets/efficiency.png'
import decs from '../../assets/direction.png'
import pers from '../../assets/personalization.png'
import ana from '../../assets/data-analytics.png'
import inno from '../../assets/rocket.png'
import trust from '../../assets/shield.png'
import exp from '../../assets/certificate.png'
import scal from '../../assets/full-screen.png'

function WhyChoose() {
    const [expandedRow, setExpandedRow] = useState(null);

    const toggleExpand = (index) => {
        if (expandedRow === index) {
            setExpandedRow(null); // Collapse the clicked row if already expanded
        } else {
            setExpandedRow(index); // Expand the clicked row
        }
    };

    return (
        <div className="whychoose-container">

            <div className='left-box'>
                <h2>Why Choose Us?</h2>
                <hr />
                <p>Discover NeuralTech, your partner for success. We blend cutting-edge technology with personalized service to deliver superior results. Trust us to drive growth and exceed expectations in Technology. Choose  for innovation, reliability, and exceptional service.</p>
                <div className='animation-box'>
                    <ul className='boxes-container'>
                        <li>
                            <div className='box' >
                                <img src={decs} alt="Logo 1"/>
                                <p>Decision</p>
                            </div>
                        </li>
                        <li>
                            <div className='box' >
                                <img src={eff} alt="Logo 1"/>
                                <p>Efficiency</p>
                            </div>
                        </li>
                        <li>
                            <div className='box' >
                                <img src={ana} alt="Logo 1"/>
                                <p>Analytics</p>
                            </div>
                        </li>
                        <li>
                            <div className='box' >
                                <img src={pers} alt="Logo 1"/>
                                <p>Personalization</p>
                            </div>
                        </li>
                        <li>
                            <div className='box' >
                                <img src={inno} alt="Logo 1"/>
                                <p>Innovation</p>
                            </div>
                        </li>
                        <li>
                            <div className='box' >
                                <img src={trust} alt="Logo 1"/>
                                <p>Trust</p>
                            </div>
                        </li>
                        <li>
                            <div className='box' >
                                <img src={exp} alt="Logo 1"/>
                                <p>Expertise</p>
                            </div>
                        </li>
                        <li>
                            <div className='box'>
                                <img src={scal} alt="Logo 1"/>
                                <p>Scalability</p>
                            </div>
                        </li>
                    </ul>
                </div>
            </div>

            <div className='right-box'>
                <div className='whychoose-content'>
                    <ul>
                        <li>
                            <div className='line'>
                                <div className='line-p'>
                                    <p>1. Drive strategic decision-making</p>
                                </div>
                                <div className='line-btn' onClick={() => toggleExpand(1)}>
                                    <p className='plusp'>{expandedRow === 1 ? '-' : '+'}</p>
                                </div>
                            </div>
                            <div className={`expanded-content ${expandedRow === 1 ? 'expanded' : ''}`}>
                                <p>Our decision-making tools provide actionable insights and predictive analytics, empowering you to navigate complexities with clarity and confidence. From optimizing resource allocation to identifying growth opportunities, NeuralTech's AI solutions are designed to support your strategic decision-making at every turn.</p>
                            </div>
                        </li>

                        <li>
                            <div className='line'>
                                <div className='line-p'>
                                    <p>2. Automate tasks efficiently</p>
                                </div>
                                <div className='line-btn' onClick={() => toggleExpand(2)}>
                                    <p className='plusp'>{expandedRow === 2 ? '-' : '+'}</p>
                                </div>
                            </div>
                            <div className={`expanded-content ${expandedRow === 2 ? 'expanded' : ''}`}>
                                <p>Efficiency is at the core of our AI solutions. We automate repetitive tasks, optimize processes, and minimize downtime to ensure smooth operations. NeuralTech's AI-driven efficiency tools empower your team to focus on innovation and value creation, driving sustainable growth and operational excellence.</p>
                            </div>
                        </li>

                        <li>
                            <div className='line'>
                                <div className='line-p'>
                                    <p>3. Utilize advanced analytics tools</p>
                                </div>
                                <div className='line-btn' onClick={() => toggleExpand(3)}>
                                    <p className='plusp'>{expandedRow === 3 ? '-' : '+'}</p>
                                </div>
                            </div>
                            <div className={`expanded-content ${expandedRow === 3 ? 'expanded' : ''}`}>
                                <p>NeuralTech's analytics solutions transform raw data into strategic insights, enabling you to anticipate market trends, customer behavior, and operational patterns. By harnessing the power of AI and machine learning, we help you make informed decisions that drive business success and foster continuous improvement.</p>
                            </div>
                        </li>

                        <li>
                            <div className='line'>
                                <div className='line-p'>
                                    <p>4. Enhance customer personalization</p>
                                </div>
                                <div className='line-btn' onClick={() => toggleExpand(4)}>
                                    <p className='plusp'>{expandedRow === 4 ? '-' : '+'}</p>
                                </div>
                            </div>
                            <div className={`expanded-content ${expandedRow === 4 ? 'expanded' : ''}`}>
                                <p>Our personalization solutions leverage AI to analyze customer preferences, behaviors, and feedback in real-time. By delivering personalized content, recommendations, and customer support, NeuralTech helps you create meaningful connections and enhance customer lifetime value. Elevate your customer experience with our personalized AI solutions.</p>
                            </div>
                        </li>

                        <li>
                            <div className='line'>
                                <div className='line-p'>
                                    <p>5. Drive continuous innovation strategies</p>
                                </div>
                                <div className='line-btn' onClick={() => toggleExpand(5)}>
                                    <p className='plusp'>{expandedRow === 5 ? '-' : '+'}</p>
                                </div>
                            </div>
                            <div className={`expanded-content ${expandedRow === 5 ? 'expanded' : ''}`}>
                                <p>Innovation is at the heart of NeuralTech's approach to AI. We continuously research and integrate the latest advancements in AI technology to deliver solutions that optimize performance and unlock new opportunities. From AI-driven automation to predictive analytics, NeuralTech empowers businesses to innovate, adapt, and thrive in a rapidly evolving digital landscape.</p>
                            </div>
                        </li>
                        <li>
                            <div className='line'>
                                <div className='line-p'>
                                    <p>6. Build trusted client relationships</p>
                                </div>
                                <div className='line-btn' onClick={() => toggleExpand(6)}>
                                    <p className='plusp'>{expandedRow === 6 ? '-' : '+'}</p>
                                </div>
                            </div>
                            <div className={`expanded-content ${expandedRow === 6 ? 'expanded' : ''}`}>
                                <p>Trust is foundational to NeuralTech's AI services. We prioritize data security, compliance, and ethical AI deployment to deliver solutions that you can rely on. With NeuralTech, you gain a trusted partner dedicated to safeguarding your data and delivering AI solutions that align with your values and objectives.</p>
                            </div>
                        </li>
                        <li>
                            <div className='line'>
                                <div className='line-p'>
                                    <p>7. Provide expert AI solutions</p>
                                </div>
                                <div className='line-btn' onClick={() => toggleExpand(7)}>
                                    <p className='plusp'>{expandedRow === 7 ? '-' : '+'}</p>
                                </div>
                            </div>
                            <div className={`expanded-content ${expandedRow === 7 ? 'expanded' : ''}`}>
                                <p>NeuralTech's team of AI experts brings extensive industry knowledge and technical expertise to every project. We collaborate closely with your team to understand your unique challenges and goals, crafting customized AI strategies that drive tangible results. Whether you need AI development, implementation, or optimization, trust our expertise to guide you through your AI journey with confidence.</p>
                            </div>
                        </li>
                        <li>
                            <div className='line'>
                                <div className='line-p'>
                                    <p>8. Ensure scalable AI deployments</p>
                                </div>
                                <div className='line-btn' onClick={() => toggleExpand(8)}>
                                    <p className='plusp'>{expandedRow === 8 ? '-' : '+'}</p>
                                </div>
                            </div>
                            <div className={`expanded-content ${expandedRow === 8 ? 'expanded' : ''}`}>
                                <p>Scalability is a key advantage of NeuralTech's AI solutions. Our scalable architecture and flexible deployment options ensure that your AI capabilities grow alongside your business. Whether you're expanding operations, entering new markets, or adapting to changing demands, NeuralTech provides the scalability and agility you need to stay competitive and future-proof your business.</p>
                            </div>
                        </li>
                    </ul>
                </div>
            </div>
        </div>
    );
}

export default WhyChoose;
