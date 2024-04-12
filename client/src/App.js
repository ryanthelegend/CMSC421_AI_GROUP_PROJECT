import React, { useState } from 'react';
import SimpleTabs from './index.js'; 

function App() {
  const [input, setInput] = useState('');
  const [response, setResponse] = useState('');
  const [loading, setLoading] = useState(false);

  const handleInputChange = (event) => {
    setInput(event.target.value);
  };

  const handleSubmit = async (endpoint) => {
    setLoading(true);
    try {
      const response = await fetch(`http://localhost:5001/${endpoint}`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ prompt: input }),
      });

      if (!response.ok) {
        throw new Error(`HTTP error, Status: ${response.status}`);
      }
      const data = response.status !== 204 ? await response.text() : {}
      try{
        jsonData = JSON.parse(data)
        setResponse(jsonData.response || "No Response body.")
      } catch (error){
        console.error('Error parsing JSON:',error)
        setResponse("Response is not in JSON Format.")
      }
    
    } catch (error) {
      console.error('Error fetching data:', error);
      setResponse("Failed to fetch response.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div>
      <SimpleTabs
        input={input}
        onInputChange={handleInputChange}
        onSubmit={handleSubmit}
        response={response}
        loading={loading}
      />
    </div>
  );
}

export default App;
