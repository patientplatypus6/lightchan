import './App.css';
import './pages/main.css';

import Main from "./pages/main"
import Biography from "./pages/biography"
import Projects from "./pages/projects"
import Thread from './pages/thread'
import Api from './api/api'
import Sidebar from './pages/components/sidebar'
import Statsbar from './pages/components/statsbar'
import Board from './pages/board'

import {
  Routes, 
  Route, 
  useNavigate,
  useRoutes, 
  useParams, 
} from "react-router-dom";
import { useEffect } from 'react';

function App() {

  const navigate = useNavigate();

  async function handleNavigate(routename) {
    console.log("value of routename: " + routename)
    navigate("../"+routename);
  } 

  return (
    <div className='mainbackground'>
      <div className='wrapper'>
        <Sidebar/>
        <Statsbar/>
        <div className='header welcomebanner'>
          Welcome to Lightchan!
        </div>
        <Routes> 
          <Route path="/" element={<Main handleNavigate={handleNavigate} />} />
          <Route path="/:boardname" element={<Main handleNavigate={handleNavigate} />} />
          <Route path="/:boardname/:threadnumber" element={<Thread />} />
        </Routes>
      </div>
      <Api/>
    </div>
  );
}

export default App;