import React from 'react';
import "./Services.css";

function Services() {
    return( 
                <div className='wrapper'>
                    <h1>Our Services</h1>
                    <hr />
                    <p>We provide a comprehensive suite of AI services designed to transform your business operations, drive innovation, and enhance decision-making.<br /> From strategic consulting to custom AI solutions, our team of experts is dedicated to delivering impactful results tailored to your specific needs.</p>
                    
                    <div className='content-box'>
                        <div className='cardbox'>
                            <i className='bx bx-message-dots bx-md'></i>
                            <h2>AI Strategy Consulting</h2>
                            <p>Develop a tailored AI roadmap to align with business goals, ensuring a smooth AI transformation.</p>
                        </div>

                        <div className='cardbox'>
                            <i className='bx bx-laptop bx-md'></i>
                            <h2>Custom AI Solution Development</h2>
                            <p>Create bespoke AI models for specific business needs, enhancing processes and delivering insights.</p>
                        </div>

                        <div className='cardbox'>
                            <i className='bx bx-data bx-md'></i>
                            <h2>Data Engineering and Management</h2>
                            <p>Optimize data infrastructure with scalable pipelines, ensuring quality and security for AI applications.</p>
                        </div>

                        <div className='cardbox'>
                            <i className='bx bx-scatter-chart bx-md'></i>
                            <h2>Machine Learning Model Training and Deployment</h2>
                            <p>Train and deploy machine learning models for high accuracy and seamless integration into production.</p>
                        </div>

                        <div className='cardbox'>
                            <i className='bx bx-bar-chart-alt bx-md'></i>
                            <h2>AI-Powered Process Automation</h2>
                            <p>Automate workflows with AI-driven solutions like RPA and chatbots to improve efficiency and reduce costs.</p>
                        </div>

                        <div className='cardbox'>
                            <i className='bx bx-notepad bx-md'></i>
                            <h2>AI Ethics and Compliance Advisory</h2>
                            <p>Ensure ethical AI practices and compliance with regulations through expert guidance and assessments.</p>
                        </div>
                    </div>
                </div>
            
        );
}

export default Services;