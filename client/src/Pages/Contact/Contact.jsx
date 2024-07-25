import React, { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import axios from 'axios';

import Nav from '../../Components/Navbar/Nav';
import HeadImg from '../../Components/HeadImg/HeadImg';
import Content1 from '../../Components/Content1/Content1';
import Card from '../../Components/Card/Card';
import Header from '../../Components/Header/Header';
import Footer from '../../Components/Footer/Footer';
import './Contact.css';

function Contact() {

    
    const [formData, setFormData] = useState({
        firstName: '',
        lastName: '',
        email: '',
        message: ''
    });
    
    const handleChange = (e) => {
        const { name, value } = e.target;
        setFormData((prevData) => ({
            ...prevData,
            [name]: value
        }));
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        // Handle form submission logic here
        alert('Message sent!');
        setFormData({ firstName: '', lastName: '', email: '', message: '' });
    };

    return (
        <div>
            <Nav />
                <div className='contact-body'>
                    <div className="contact-container">
                        <h1>Contact Us</h1>
                        <form className="contact-form" onSubmit={handleSubmit}>
                        <div className="form-group name-group">
                            <div className="name-field">
                                <label htmlFor="firstName">First Name</label>
                                <input
                                    type="text"
                                    id="firstName"
                                    name="firstName"
                                    value={formData.firstName}
                                    onChange={handleChange}
                                    required
                                />
                            </div>
                            <div className="name-field">
                                <label htmlFor="lastName">Last Name</label>
                                <input
                                    type="text"
                                    id="lastName"
                                    name="lastName"
                                    value={formData.lastName}
                                    onChange={handleChange}
                                    required
                                />
                            </div>
                        </div>

                        <div className="form-group">
                            <label htmlFor="email">Email</label>
                            <input
                                type="email"
                                id="email"
                                name="email"
                                value={formData.email}
                                onChange={handleChange}
                                required
                            />
                        </div>
                        <div className="form-group">
                            <label htmlFor="message">Message</label>
                            <textarea
                                id="message"
                                name="message"
                                value={formData.message}
                                onChange={handleChange}
                                required
                            ></textarea>
                        </div>
                        <button type="submit">Send Message</button>
                        </form>
                    </div>
                    
                    <div className='my-contact-container'>
                        <div className='our-address'>
                            <h3>OUR ADDRESS</h3>
                            <p>123 Maple Street Springfield, IL 62701</p>
                        </div>

                        <div className='our-social'>
                            <h3>OUR SOCIAL</h3>
                            <div className='our-social-links'>
                                <a href="#"><i className='fab fa-facebook-f'></i></a>
                                <a href="#"><i className='fab fa-twitter'></i></a>
                                <a href="#"><i className='fab fa-instagram'></i></a>
                                <a href="#"><i className='fab fa-linkedin-in'></i></a>
                            </div>
                        </div>

                        <div className='our-email'>
                            <h3>EMAIL US</h3>
                            <p>For Product Question/Concerns, Brand, <br />
                               Information & General inquiries: <br />
                               <span id='email'>info@neuraltech.net</span> <br />
                               <br />
                               Visit our corporate website:<br />
                               www.neuraltech.com</p>
                        </div>
                    </div>
            
                </div>
            <Footer />
        </div>)
}

export default Contact;