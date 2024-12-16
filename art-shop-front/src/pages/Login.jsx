import React, { useState } from 'react';
import { login } from '../services/api';

const Login = () => {
  const [mobile, setMobile] = useState('');
  const [otp, setOtp] = useState('');
  const [isOTPRequested, setIsOTPRequested] = useState(false);

  const handleRequestOTP = async () => {
    try {
      await login({ mobile });
      setIsOTPRequested(true);
    } catch (err) {
      console.error(err);
    }
  };

  const handleVerifyOTP = async () => {
    try {
      const response = await login({ mobile, otp });
      localStorage.setItem('token', response.data.access);
      window.location.href = '/';
    } catch (err) {
      console.error(err);
    }
  };

  return (
    <div>
      <h2>Login</h2>
      <input
        type="text"
        placeholder="Mobile"
        value={mobile}
        onChange={(e) => setMobile(e.target.value)}
      />
      {isOTPRequested && (
        <input
          type="text"
          placeholder="OTP"
          value={otp}
          onChange={(e) => setOtp(e.target.value)}
        />
      )}
      <button onClick={isOTPRequested ? handleVerifyOTP : handleRequestOTP}>
        {isOTPRequested ? 'Verify OTP' : 'Request OTP'}
      </button>
    </div>
  );
};

export default Login;
