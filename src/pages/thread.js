import React, { useEffect, useState } from 'react';
import {
  RecoilRoot,
  atom,
  selector,
  useRecoilState,
  useRecoilValue,
} from 'recoil';

import {
  matchPath,
  useLocation
} from "react-router-dom";

import {
  retrieveAllRepliesByID, 
  replyGetState, 
  replyPostState,
  commentGetState, 
  commentGetResponse,  commentPostState, commentPostResponse, retrieveAllComments
} from '../state/state'

import './thread.css'
import './main.css'

import PostCommentContainer from './components/postcommentcontainer';
import CommentContainer from './components/commentcontainer';
import ReplyContainer from './components/replycontainer';
import PostReplyContainer from './components/postreplycontainer';


function ReplyList(){

  const [replyretrieveallbyid, setReplyRetrieveAllByID] = useRecoilState(retrieveAllRepliesByID);
  const [dataArray, setDataArray] = useState([])

  useEffect(()=>{
    console.log("&&&&&&&&&&&&&&&&&&&&&&&&&&")
    console.log('value of replyretrieveallbyid: ', replyretrieveallbyid)
    console.log("&&&&&&&&&&&&&&&&&&&&&&&&&&")
    setDataArray(replyretrieveallbyid.response.data)
  }, [replyretrieveallbyid])    

  return( 
    <div style={{textAlign: 'center'}}>
      {dataArray!=undefined?dataArray.map((reply, key)=>{
        return(
          <div key={key}>
            <ReplyContainer
              reply={reply}
            />
            <br/>
          </div>  
        )
      }):<div>Some error</div>}
    </div>
  )

}

function Thread(){

  const [getreply, setGetReply] = useRecoilState(replyGetState);
  const [postreply, setPostReply] = useRecoilState(replyPostState);

  const [getcomment, setGetComment] = useRecoilState(commentGetState);
  const [commentgetresponse, setCommentGetResponse] = useRecoilState(commentGetResponse)
  const [postcomment, setPostComment] = useRecoilState(commentPostState);
  const [commentpostresponse, setCommentPostResponse] = useRecoilState(commentPostResponse);
  const [commentretrieveall, setCommentRetrieveAll] = useRecoilState(retrieveAllComments);
  const [replyretrieveallbyid, setReplyRetrieveAllByID] = useRecoilState(retrieveAllRepliesByID);


  const [threadnum, setThreadnum] = useState('')
  const location = useLocation();

  useEffect(()=>{
    console.log("*****************")
    console.log("replyretrieveallbyid: ", replyretrieveallbyid)
    console.log("*****************")
  }, [replyretrieveallbyid])

  useEffect(()=>{
    console.log('inside commentgetresponse and value of response: ', commentgetresponse)
  }, [commentgetresponse])

  useEffect(()=>{
    console.log('value of location: ', location)
    setThreadnum(location.pathname.replace("/thread/", ""))
    setGetComment({id: location.pathname.replace("/thread/", ""), submit: true})
    setReplyRetrieveAllByID({comment_id: location.pathname.replace("/thread/", ""), response: {}, submit: true})
  }, [])

  useEffect(()=>{
    console.log("the value of postreply is: ", postreply)
  }, [postreply])

  return(
    <div className='thread'> 
      <div className='threadbanner'>
        Thread {threadnum}  
      </div>
      <PostReplyContainer
        reply={postreply}
        submitReply={(e)=>{setPostReply({...e, ...{comment_id:threadnum}})}}
      />
      <br/>
      ~~~ Comment ~~~
      <br/>
      {commentgetresponse.response.data!=undefined?
        <CommentContainer
          showthread={false}
          handleNavigate={()=>{}}
          comment={commentgetresponse.response.data}
        />:<div/>}
      <br/>
      ~~~ Replies ~~~
      <br/>
      <ReplyList/>
    </div>
  )

}

export default Thread;