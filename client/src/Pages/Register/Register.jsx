import React, {useState, useEffect} from 'react';
import { useNavigate } from 'react-router-dom';
import axios from 'axios';
import './Register.css'
import logo_ai from '../../assets/ai.png'


function Register() {

    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [confPassword, setConfPassword] = useState('');
    const [message, setMessage] = useState('');
    const [messageColor, setMessageColor] = useState('');

    const navigate = useNavigate();

    const LoginPage = () => {
        navigate("/");
    };

    const handleRegister = async (event) => {
        console.log('submit success');
        console.log(email);
        console.log(password);
        console.log(confPassword);
        event.preventDefault();

        if (password !== confPassword) {
            setMessage('Passwords do not match');
            setMessageColor('red');
            return;
        }

        try {
            const response = await axios.post('http://localhost:5000/register', {email, password});
            // console.log('send api success');
            // console.log(response.data.message);
            setMessage(response.data.message);
            if (response.data.message === 'Your registration already successfully') {
                setMessageColor('#1fc035');
                navigate('/register');
            } else if (response.data.message === 'Email already exists. Try logging in.') {
                setMessageColor('red');
                navigate('/register');
            }
        } catch (error) {
            console.log(error.response.data.message);
            setMessage('Database connection error');
            setMessageColor('red');
        }

    };

    




    return (<div className="register-container">
                <div className='left'>
                    <img src={logo_ai} alt="logo" />
                    <h1>NeuralTech</h1>
                    <p>Our AI web application leverages the latest advancements in artificial intelligence to provide intuitive, user-friendly interfaces and powerful backend processing. Whether you are looking to enhance user experience or automate complex tasks, 
                        our platform offers unparalleled efficiency and ease of use.</p>
                </div>

                <div className='right'> 
                    <h2>Register</h2>
                    <p>Already have an account? <span className='login-link' onClick={LoginPage}>Login</span></p>
                    <form className="form" onSubmit={handleRegister}>

                        <div className="input-group">
                            <label htmlFor="email">Email</label>
                            <input 
                            type="email" 
                            id="email" 
                            name="email" 
                            value={email} 
                            onChange={(e) => setEmail(e.target.value)} 
                            required />
                        </div>

                        <div className="input-group">
                            <label htmlFor="password">Password</label>
                            <input 
                            type="password" 
                            id="password" 
                            name="password"
                            value={password}
                            onChange={(e) => setPassword(e.target.value)}
                            required />
                        </div>

                        <div className="input-group">
                            <label htmlFor="password">Confirm Password</label>
                            <input 
                            type="password" 
                            id="conf-password" 
                            name="conf-password"
                            value={confPassword}
                            onChange={(e) => setConfPassword(e.target.value)}
                            required />
                        </div>   
                        <button type="submit">Register</button>
                    </form>
                    {message && <p style={{color: messageColor, fontSize: "8pt", marginTop: "8px"}}>{message}</p>}
                </div>
            </div>)
}

export default Register;