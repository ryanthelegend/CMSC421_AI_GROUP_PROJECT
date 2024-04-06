import React, {useEffect, useState} from 'react'
import { generateSummary  } from './services/summaryServices'

function App() {
  const [input, setInput] = useState('');
  const [summary, setSummary] = useState('');
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setSummary(''); 
    try {
      const data = await generateSummary({ prompt: input });
      setSummary(data.response);
    } catch (error) {
      console.error('There was an error generating the summary:', error);
    }
    setLoading(false);
  };

  return (
    <div>
      <form onSubmit={handleSubmit}>
        <textarea
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="Enter text or URL"
        />
        <button type="submit" disabled={loading}>
          Summarize
        </button>
      </form>

      {loading && <p>Loading...</p>}

      {summary && (
        <div>
          <h2>Summary</h2>
          <p>{summary}</p>
        </div>
      )}
    </div>
  );
}

/* 
function App() {
  
  const [backendData, setBackendData] = useState([{}])

  useEffect (() => {
    fetch("/api").then(
      response => response.json()
    ).then(
      data => { 
        setBackendData(data)
      }

    )
  }, [])

  return (
    <div>

      {(typeof backendData.users === 'undefined') ? ( 

        <p>Loading...</p>
      ): (
        backendData.users.map((user, i) => (
          <p key={i}>{user}</p>
        ))
        )}
      

    </div>
  )
}*/

export default App