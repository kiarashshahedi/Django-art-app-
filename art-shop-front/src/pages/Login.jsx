import React, { useState } from 'react';
import axios from 'axios';

const Login = () => {
    const [mobile, setMobile] = useState('');
    const [otp, setOTP] = useState('');
    const [step, setStep] = useState(1);

    const handleGenerateOTP = async () => {
        const response = await axios.post('/api/users/generate-otp/', { mobile });
        if (response.status === 200) setStep(2);
    };

    const handleVerifyOTP = async () => {
        const response = await axios.post('/api/users/verify-otp/', { mobile, otp });
        if (response.status === 200) {
            localStorage.setItem('access_token', response.data.access);
            alert('Logged in successfully!');
        }
    };

    return (
        <div>
            {step === 1 ? (
                <>
                    <input 
                        type="text" 
                        placeholder="Mobile" 
                        value={mobile} 
                        onChange={(e) => setMobile(e.target.value)} 
                    />
                    <button onClick={handleGenerateOTP}>Send OTP</button>
                </>
            ) : (
                <>
                    <input 
                        type="text" 
                        placeholder="Enter OTP" 
                        value={otp} 
                        onChange={(e) => setOTP(e.target.value)} 
                    />
                    <button onClick={handleVerifyOTP}>Verify OTP</button>
                </>
            )}
        </div>
    );
};

export default Login;
