import React, { useState } from 'react';
import CartItem from '../components/CartItem';

const Cart = () => {
  const [cart, setCart] = useState([]);

  const handleUpdateQuantity = (id, quantity) => {
    // Update quantity logic here
  };

  const handleRemoveItem = (id) => {
    // Remove item logic here
  };

  return (
    <div>
      <h2>Your Cart</h2>
      {cart.map((item) => (
        <CartItem key={item.id} item={item} onUpdate={handleUpdateQuantity} onRemove={handleRemoveItem} />
      ))}
    </div>
  );
};

export default Cart;
