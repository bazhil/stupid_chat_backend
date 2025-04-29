import React, { useState } from 'react';
import './App.css'

function App() {
  const [question, setQuestion] = useState('');
  const [answer, setAnswer] = useState('');

  const handleInputChange = (event) => {
    setQuestion(event.target.value);
  };

  const handleSubmit = async () => {
    try {
      const response = await fetch('http://localhost:8000/get_answer', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ question }),
      });

      if (response.ok) {
        const data = await response.json();
        setAnswer(data.answer);
      } else {
        setAnswer('Error fetching answer');
      }
    } catch (error) {
      setAnswer('Error: ' + error.message);
    }
  };

  return (
    <div className="App">
      <input type="text" value={question} onChange={handleInputChange} placeholder="Enter your question" />
      <button onClick={handleSubmit}>Get Answer</button>
      {answer && (
        <div className="answer">
            <p><b>Answer:</b> {answer}</p>
        </div>)}
    </div>
  );
}

export default App;
