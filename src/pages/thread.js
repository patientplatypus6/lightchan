import React, { useEffect, useState } from 'react';
import {
  RecoilRoot,
  atom,
  selector,
  useRecoilState,
  useRecoilValue,
} from 'recoil';

import './thread.css'
import './main.css'

import {
  matchPath,
  useLocation
} from "react-router-dom";

import {
  commentGetState, 
  commentGetResponse,  commentPostState, commentPostResponse, retrieveAllComments
} from '../state/state'

function Thread(){

  const [getcomment, setGetComment] = useRecoilState(commentGetState);
  const [commentgetresponse, setCommentGetResponse] = useRecoilState(commentGetResponse)
  const [postcomment, setPostComment] = useRecoilState(commentPostState);
  const [commentpostresponse, setCommentPostResponse] = useRecoilState(commentPostResponse);
  const [commentretrieveall, setCommentRetrieveAll] = useRecoilState(retrieveAllComments);


  const [threadnum, setThreadnum] = useState('')
  const location = useLocation();

  useEffect(()=>{
    console.log('value of location: ', location)
    setThreadnum(location.pathname.replace("/thread/", ""))
    
  }, [])

  return(
    <div className='thread'> 
      <div className='threadbanner'>
        Thread {threadnum}  
      </div>
    </div>
  )

}

export default Thread;