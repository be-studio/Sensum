import React from 'react';
import logo from './logo.svg';
import './App.css';
import { Link } from "react-router-dom";
import { useCsrfQuery } from "./Auth/hooks/useCsrfQuery";

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Welcome to Sensum!
        </p>
        <Link to="login">Login</Link>
      </header>
    </div>
  );
}

export default App;
