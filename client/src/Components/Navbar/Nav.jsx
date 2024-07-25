import React, {useState} from 'react';
import { useNavigate } from 'react-router-dom';
import "./Nav.css";
import logo_ai from '../../assets/ai.png'
import search_icon_dark from '../../assets/search-b.png'



function Nav() {
    const [dropdownVisible, setDropdownVisible] = useState(false);
    const navigate = useNavigate();

    // navigate
    const homePage = () => {
        navigate("/home");
    };

    const loginPage = () => {
        navigate("/");
    };

    const modelsPage = () => {
        navigate("/models");
    };

    const aboutPage = () => {
        navigate("/about");
    };

    const contactPage = () => {
        navigate("/contact");
    };

    const classifyPage = () => {
        navigate("/classify")
    }

    const objectPage = () => {
        navigate("/object")
    }

    const segmentPage = () => {
        navigate("/segment")
    }


    // state
    const showDropdown = () => {
        setDropdownVisible(true);
    };

    const hideDropdown = () => {
        setDropdownVisible(false);
    };
    
    return(
                <div className="navbar">
                    <div className='logo'>
                        <img src={logo_ai} alt="logo" />
                        <h2>NeuralTech</h2>
                    </div>
                    
                    <ul>
                        <li onClick={homePage}>Home</li>
                        <li onClick={modelsPage}>Models</li>
                        <li 
                            onMouseOver={showDropdown} 
                            onMouseOut={hideDropdown}>
                                Features
                                {dropdownVisible && (
                                    <ul className='dropdown'>
                                        <li onClick={classifyPage}>Classification</li>
                                        <li onClick={objectPage}>Object Detection</li>
                                        <li onClick={segmentPage}>Segmentation</li>
                                    </ul>
                                )}
                        </li>
                        <li onClick={aboutPage}>About</li>
                        <li onClick={contactPage}>Contact Us</li>
                    </ul>
                

                    <div className="search-box">
                        <input type="text" placeholder="Search"/>
                        <img src={search_icon_dark} alt="" />
                    </div>

                    <div className="log-out" onClick={loginPage}>
                        <p>Log Out</p>
                    </div>

            
                </div>
                
           )
}

export default Nav;