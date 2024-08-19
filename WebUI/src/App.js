import React, { useState, useEffect } from 'react';

function App() {
  const [data, setData] = useState('');
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');

  useEffect(() => {
    fetch('http://localhost:8080/')
      .then(response => response.json())
      .then(data => {
        setData(data.message); // Assuming your API returns an object with a message property
        setLoading(false);
      })
      .catch(err => {
        setError('Failed to fetch data from Ollama');
        setLoading(false);
      });
  }, []);

  if (loading) return <p>Loading...</p>;
  if (error) return <p>{error}</p>;

  return (
    <div>
      <h1>Welcome to WebUI</h1>
      <p>Data from Ollama: {data}</p>
    </div>
  );
}

export default App;
