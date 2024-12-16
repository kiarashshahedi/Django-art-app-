import React from 'react';

const CartItem = ({ item, onUpdate, onRemove }) => {
  return (
    <div className="cart-item">
      <h4>{item.product.name}</h4>
      <p>Price: ${item.product.price}</p>
      <p>Quantity: {item.quantity}</p>
      <button onClick={() => onUpdate(item.id, item.quantity + 1)}>+</button>
      <button onClick={() => onUpdate(item.id, item.quantity - 1)}>-</button>
      <button onClick={() => onRemove(item.id)}>Remove</button>
    </div>
  );
};

export default CartItem;
