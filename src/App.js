import './App.css';
import './pages/main.css';

import Main from "./pages/main"
import Thread from './pages/thread'
import Sidebar from './pages/components/sidebar'
import Statsbar from './pages/components/statsbar'

import {
  Routes, 
  Route, 
  useNavigate,
  useRoutes, 
  useLocation,
  useParams, 
} from "react-router-dom";
import {
  RecoilRoot,
  atom,
  selector,
  useRecoilState,
  useRecoilValue,
} from 'recoil';
import {retrieveAllComments} from './state/state'

import { useEffect } from 'react';

function App() {

  const navigate = useNavigate();
  const [commentretrieveall, setCommentRetrieveAll] = useRecoilState(retrieveAllComments);

  const location = useLocation();

  async function handleNavigate(routename) {
    console.log("value of routename: " + routename)
    navigate("../"+routename);
    retrieveComments()
  }

  const retrieveComments = () => {
    setCommentRetrieveAll({
      submit: true,
      response: {}
    })
  }

  //should be updated in NGINX but can live here for the moment
  useEffect(()=>{
    if(window.location.href.includes('http://')){
	let newpath = window.location.href.replace('http://', 'https://')
	window.location.replace(newpath)
    }
  }, [])

  return (
    <div className='mainbackground'>
      <div className='wrapper'>
        <Sidebar
          handleNavigate={(board)=>{
            handleNavigate(board)
          }}
        />
        <Statsbar/>
        <div className='header welcomebanner'>
          Welcome to Lightchan!
        </div>
        <Routes> 
          <Route path="/" 
            element={<Main 
              handleNavigate={handleNavigate} 
              retrieveComments={retrieveComments}
            />} 
          />
          <Route path="/:boardname" 
            element={<Main 
              handleNavigate={handleNavigate} 
              retrieveComments={retrieveComments}
            />} 
          />
          <Route path="/:boardname/:threadnumber" element={<Thread />} />
        </Routes>
      </div>
    </div>
  );
}

export default App;
