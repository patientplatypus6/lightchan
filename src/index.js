import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import Api from './api/api';
import reportWebVitals from './reportWebVitals';

import {
  BrowserRouter as Router,
  Routes, 
  Route, 
  useNavigate,
  useRoutes,
  BrowserRouter
} from "react-router-dom";
import { RecoilRoot } from 'recoil';

ReactDOM.render(
  <React.StrictMode>
    <RecoilRoot>
      <BrowserRouter>
        <App />
        <Api />
      </BrowserRouter>
    </RecoilRoot>
  </React.StrictMode>,
  document.getElementById('root')
);

reportWebVitals();
