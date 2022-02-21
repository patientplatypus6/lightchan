import './App.css';

import Main from "./pages/main"
import Biography from "./pages/biography"
import Projects from "./pages/projects"

import {
  Routes, 
  Route, 
  useNavigate,
  useRoutes
} from "react-router-dom";

function App() {

  const navigate = useNavigate();

  async function handleNavigate(routename) {
    console.log("value of routename: " + routename)
    navigate("../"+routename, { replace: true });
  }

  function navbar(){
    return(
      <div className='navbar'>
        <div
        className='navbutton'
        onClick={() => handleNavigate('/')}>
          Main
        </div>
        <div
        className='navbutton'
        onClick={() => handleNavigate('projects')}>
          Projects
        </div>
        <div
        className='navbutton'
        onClick={() => handleNavigate('biography')}>
          Biography
        </div>
      </div>
    )
  }

  return (
    <div className='mainbackground'>
      {navbar()}
      <Routes>
        <Route path="/" element={<Main />} />
        <Route path="/projects" element={<Projects />} />
        <Route path="/biography" element={<Biography />} />
      </Routes>
    </div>
  );
}

export default App;