import axios from 'axios';

// Create Axios instance
const API = axios.create({
  baseURL: 'http://127.0.0.1:8000/api/',
});

// Add authorization token to requests
API.interceptors.request.use((req) => {
  const token = localStorage.getItem('token');
  if (token) req.headers.Authorization = `Bearer ${token}`;
  return req;
});

// User API
export const login = (data) => API.post('/users/token/', data);
export const signup = (data) => API.post('/users/register/', data);

// Product API
export const getProducts = (params) => API.get('/products/', { params });
export const getProductDetail = (id) => API.get(`/products/${id}/`);
export const createProduct = (data) => API.post('/products/', data);
export const updateProduct = (id, data) => API.put(`/products/${id}/`, data);
export const deleteProduct = (id) => API.delete(`/products/${id}/`);

// Order API
export const getOrders = () => API.get('/orders/');
export const createOrder = (data) => API.post('/orders/', data);

export default API;
