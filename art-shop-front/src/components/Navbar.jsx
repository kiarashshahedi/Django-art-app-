import React from 'react';
import { Link } from 'react-router-dom';

const Navbar = () => {
  const isLoggedIn = Boolean(localStorage.getItem('token'));
  const handleLogout = () => {
    localStorage.removeItem('token');
    window.location.reload();
  };

  return (
    <nav>
      <h1>Art Shop</h1>
      <Link to="/">Home</Link>
      {isLoggedIn ? (
        <>
          <Link to="/dashboard">Dashboard</Link>
          <Link to="/orders">Orders</Link>
          <button onClick={handleLogout}>Logout</button>
        </>
      ) : (
        <>
          <Link to="/login">Login</Link>
          <Link to="/signup">Signup</Link>
        </>
      )}
    </nav>
  );
};

export default Navbar;
