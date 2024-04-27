import React, { useState } from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';

import { AppBar, Tabs, Tab, Box, Button, TextareaAutosize } from "@material-ui/core";

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);

function TabPanel({children,value,index}) {
  return (
    <div
      role="tabpanel"
      hidden={value !== index}
      id={`simple-tabpanel-${index}`}
      aria-labelledby={`simple-tab-${index}`}
    >
      {value === index && (
        <Box p={3}>
          {children}
        </Box>
      )}
    </div>
  );
}

export default function SimpleTabs({ input,onInputChange,onSubmit,response,loading }) {
  const [value, setValue] = useState(0);

  const handleChange = (event, newValue) => {
    setValue(newValue);
  };

  return (
    <div>
      <AppBar position="static">
        <Tabs value={value} onChange={handleChange}>
          <Tab label="Chatbox" />
          <Tab label="PDF Summarizer" />
          <Tab label="URL Summarizer" />
        </Tabs>
      </AppBar>
      <TabPanel value={value} index={0}>
        <h3>Chatbox</h3>
        <TextareaAutosize 
          aria-label="empty textarea" 
          placeholder="Enter your message here..." 
          value = {input}
          onChange = {onInputChange}
        />
        <Button 
          variant="contained" 
          color="primary"
          className = "button-hover-effect"
          onClick = {()=>onSubmit('generate')}
        >
          Submit
        </Button>
        {loading && <p>Loading...</p>}
        {response && <div><h4>Response:</h4><p>{response}</p></div>}
      </TabPanel>
      <TabPanel value={value} index={1}>
        <h3>PDF Summarizer</h3>
        <p>This is where the PDF summarizer will be.</p>
      </TabPanel>
      <TabPanel value={value} index={2}>
        <h3>URL Summarizer</h3>
        <p>This is where the URL summarizer will be.</p>
      </TabPanel>
    </div>
  );
}

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
