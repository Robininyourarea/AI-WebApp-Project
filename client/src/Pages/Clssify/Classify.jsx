import React, {useState, useEffect} from 'react';
import axios from 'axios';
import Nav from '../../Components/Navbar/Nav';
import ProgressBar from '../../Components/ProgressBar/ProgressBar';
import './Classify.css'
import upload from '../../assets/upload.png'
import barchart from '../../assets/bar-chart.png'
import { Oval } from 'react-loader-spinner'

function Classify() {
    const [image, setImage] = useState(null);
    const [imageUrl, setImageUrl] = useState(null);
    const [prediction, setPrediction] = useState(null);
    const [loading, setLoading] = useState(false);
    const [model, setModel] = useState('');
    const [dropdownOpen, setDropdownOpen] = useState(false);
    const [placeHolder, setPlaceHolder] = useState('Select Model');
    const [modelData, setModelData] = useState({ top1Accuracy: '-', top5Accuracy: '-', Parameters: '-' });

    const handleImageUpload = (event) => {
        console.log('this function triggerd')
        const file = event.target.files[0];
        if (file) {
            setImage(file);
            setImageUrl(URL.createObjectURL(file));

            // Convert selected file to base64
            const reader = new FileReader();
            reader.readAsDataURL(file);
            reader.onloadend = () => {
                const base64Data = reader.result.split(',')[1];
                setImage(base64Data); // Set the image state to base64 encoded string
            };
        }
    };

    const handleDisplayClick = () => {
        document.getElementById('fileInput').click();
    };

    const handlePrediction = async () => {
        setPrediction(null);
        if (!image) {
            alert('Please upload an image first.')
            return;
        }

        setLoading(true);

        try {
        
            
            // console.log(image) // image in this state is base64
            const response = await axios.post('http://localhost:5000/cls_upload-image', { image, model });
            console.log(response.data);
            setPrediction(response.data);

        } catch (error) {
            console.error('Error predicting image:', error);
            alert('Failed to predict image. Please try again.');
        } finally {
            setLoading(false);
        }
    }

    const handleNewImageUpload = () => {
        // Clear the image state and URL
        setImage(null);
        setImageUrl(null);
        setLoading(false)
        // Trigger the file input click
        handleDisplayClick();
    };

    const handleModelSelect = (selectedModel) => {
        setModel(selectedModel);
        setPlaceHolder(selectedModel);
        setModelData(models[selectedModel]);
        setDropdownOpen(false);
    }

    const models = {
        'Efficientnet B0': { top1Accuracy: '77.7%', top5Accuracy: '93.5%', Parameters: '5.3M' },
        'Efficientnet B1': { top1Accuracy: '78.6%', top5Accuracy: '94.2%', Parameters: '7.8M' },
        'Efficientnet B2': { top1Accuracy: '80.6%', top5Accuracy: '95.3%', Parameters: '9.1M' },
        'Efficientnet B3': { top1Accuracy: '82.0%', top5Accuracy: '96.0%', Parameters: '12.2M' }
    };

    return(<div>
                <Nav />
                
                <div className='classification-features'>


                    {/* section 1 */}
                    <div className='dashboard-body'>
                        <div className='control-panel'>
                            <div className='model-header'>
                                <h2>Classification Model</h2>
                            </div>
                            <div className='model-dropdown-box'>
                                
                                <input 
                                    type="text" 
                                    className='textBox' 
                                    placeholder={placeHolder}
                                    readonly
                                    onClick={() => setDropdownOpen(!dropdownOpen)}
                                />

                                
                                {dropdownOpen && (
                                <div className='model-option'>
                                    {Object.keys(models).map((modelKey) => (
                                        <div key={modelKey} onClick={() => handleModelSelect(modelKey)}>
                                            {modelKey}
                                        </div>
                                    ))}
                                </div>
                            )}
                            </div>
                            {!image && <button className='upload-button' onClick={handleDisplayClick}>Upload image</button>}
                            {image && <button className='upload-button' onClick={handleNewImageUpload}>Upload new image</button>}
                            {image && <button className='predict-button' onClick={handlePrediction}>Let's Predict</button>}
                            
                        </div>

                        
                        <div className='dashboard-container'>
                            {Object.entries(modelData).map(([key, value], index) => (
                                <div className='dashboard-card' key={index}>
                                    <div className='dashboard-value'>{value}</div>
                                    <div className='dashboard-title'>{key.replace(/([A-Z])/g, ' $1')}</div>
                                </div>
                            ))}
                        </div>
                        
                    </div>


                    {/* section 2 */}
                    <div className='prediction-body'>

                        <div className='upload-box'>
                            <div className='upload-container'>
                                {imageUrl ? null : (<img src={upload} alt="upload-logo" className='upload-logo'/>)}
                                
                                {imageUrl ? (<img src={imageUrl} alt="uploaded-img" className='uploaded-img'/>) : 
                                            (<p> upload your image</p>)}
                            </div>

                            <input 
                                type="file" 
                                id='fileInput'
                                style={{display: 'none'}}
                                onChange = {handleImageUpload}
                            />
                        
                
                        </div>

                        {/* <div className='buttons-box'>
                            <div className='buttons'>
                                {!image && <button className='upload-button' onClick={handleDisplayClick}>Upload new image</button>}
                                {image && <button className='upload-button' onClick={handleNewImageUpload}>Upload new image</button>}
                                {image && <button className='predict-button' onClick={handlePrediction}>Let's Predict</button>}
                            </div>
                        </div> */}



                        <div className='prediction-box'>
                                {prediction ? (
                                <div>
                                    <ProgressBar
                                    label1={prediction.Class1}
                                    value1={prediction.Prob1}
                                    label2={prediction.Class2}
                                    value2={prediction.Prob2}
                                    label3={prediction.Class3}
                                    value3={prediction.Prob3}
                                    label4={prediction.Class4}
                                    value4={prediction.Prob4}
                                    />
                                </div>
                                ) : (
                                <div className='unpredict'>
                                    {loading ? (
                                    <Oval
                                        height={80}
                                        width={80}
                                        color="#5A639C"
                                        wrapperStyle={{}}
                                        wrapperClass=""
                                        visible={true}
                                        ariaLabel='oval-loading'
                                        secondaryColor="#9B86BD"
                                        strokeWidth={2}
                                        strokeWidthSecondary={2}
                                    />
                                    ) : (
                                    <>
                                        <img src={barchart} alt="upload-logo" className='upload-logo' />
                                        <p>prediction</p>
                                    </>
                                    )}
                                </div>
)}
                            
                        </div>
                    </div>
                </div>

            </div>);
}

export default Classify;