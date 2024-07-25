import React, {useState, useEffect} from 'react';
import { useNavigate } from 'react-router-dom';
import axios from 'axios';
import './Login.css'
import logo_ai from '../../assets/ai.png'

function Login() {

    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [message, setMessage] = useState('');
    const navigate = useNavigate();

    const RegisterPage = () => {
        navigate("/register");
    };

    const handleLogin = async (event) => {
        console.log('submit success');
        console.log(email);
        console.log(password);
        event.preventDefault();

        try {
            const response = await axios.post('http://localhost:5000/login', {email, password });
            console.log('send api success');
            console.log(response.data.message);
            setMessage(response.data.message);
            if (response.data.message === 'Login successful') {
                navigate('/home');
            } else if (response.data.message === 'Incorrect password') {
                navigate('/');
            }
        } catch (error) {
            console.log('fail');
            setMessage(error.response.data.message);
        }
    };





    return (<div className="login-container">
                <div className='left'>
                    <img src={logo_ai} alt="logo" />
                    <h1>NeuralTech</h1>
                    <p>Our AI web application leverages the latest advancements in artificial intelligence to provide intuitive, user-friendly interfaces and powerful backend processing. Whether you are looking to enhance user experience or automate complex tasks, 
                        our platform offers unparalleled efficiency and ease of use.</p>
                </div>

                <div className='right'> 
                    <h2>Login to your account</h2>
                    <p>Don't have an account? <span className='register' onClick={RegisterPage}>Sign Up</span></p>
                    <form className="form" onSubmit={handleLogin}>
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
                        <button type="submit">Login</button>
                    </form>
                    {message && <p style={{color: "red", fontSize: "8pt", marginTop: "8px"}}>{message}</p>}
                </div>
            </div>)
}

export default Login;