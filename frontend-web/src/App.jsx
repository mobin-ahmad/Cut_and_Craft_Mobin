import React, { useState } from 'react';
import axios from 'axios';

axios.defaults.baseURL = 'http://127.0.0.1:8000';

function App() {
  const [orderId, setOrderId] = useState('');
  const [status, setStatus] = useState('');

  const createOrder = async () => {
    const res = await axios.post('/orders/', {
      customer_name: 'Test Customer',
      measurements: { chest: 38, waist: 32 /* full 22 */ },
      fabric_code: 'FAB001',
      quantity_meters: 3.5,
      outlet: 'Lahore Defence'
    });
    setOrderId(res.data.id);
    setStatus(res.data.status);
  };

  const advanceFlow = async (step) => {
    await axios.post(`/orders/${orderId}/${step}`);
    const res = await axios.get(`/orders/${orderId}`);
    setStatus(res.data.status);
  };

  return (
    <div style={{ padding: '20px', background: '#f0f0f0' }}>
      <h1 style={{ color: '#003087' }}>Cut & Craft by Zoi Solution</h1>
      <p>Full MTM Flow Live – Test Your Diagram!</p>
      <button onClick={createOrder} style={{ background: 'orange', color: 'white', padding: '10px' }}>Start Order (Blue: Fed in System)</button>
      {orderId && (
        <div>
          <p>Order ID: {orderId} | Status: {status}</p>
          <button onClick={() => advanceFlow('approve')} style={{ background: 'lightblue' }}>Approve (Light Blue)</button>
          <button onClick={() => advanceFlow('sync-material')} style={{ background: 'orange' }}>Sync Material (Orange)</button>
          <button onClick={() => advanceFlow('start-stitching')} style={{ background: 'green' }}>Start Stitching (Green)</button>
          <button onClick={() => advanceFlow('dispatch')} style={{ background: 'green' }}>Dispatch</button>
          <button onClick={() => advanceFlow('handover')} style={{ background: 'blue' }}>Hand Over (Blue Loop)</button>
        </div>
      )}
      <div style={{ marginTop: '20px' }}>
        <h2>Live Flow Diagram</h2>
        <svg width="800" height="400" style={{ border: '1px solid gray' }}>
          {/* Simple SVG viz of your diagram - nodes & arrows */}
          <rect x="50" y="50" width="100" height="50" fill="#003087" stroke="black">
            <text x="75" y="75" fill="white">User Login</text>
          </rect>
          <line x1="100" y1="100" x2="200" y2="100" stroke="black" markerEnd="url(#arrow)" />
          {/* Add more rects/lines for full diagram - Dynasty coded 22 nodes */}
          <defs>
            <marker id="arrow" markerWidth="10" markerHeight="10" refX="0" refY="3" orient="auto">
              <path d="M0,0 L0,6 L9,3 z" fill="black" />
            </marker>
          </defs>
        </svg>
      </div>
    </div>
  );
}

export default App;