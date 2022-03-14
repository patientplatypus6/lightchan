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
  replyPostState,
  commentGetState, 
  board,
  commentGetResponse
} from '../state/state'

import './thread.css'
import './main.css'

import PostCommentContainer from './components/postcommentcontainer';
import CommentContainer from './components/commentcontainer';
import ReplyContainer from './components/replycontainer';
import PostReplyContainer from './components/postreplycontainer';

function ReplyList(){

  const [commentgetresponse, setCommentGetResponse] = useRecoilState(commentGetResponse)

  return( 
    <div style={{textAlign: 'center'}}>
      {commentgetresponse.replies!=[]?commentgetresponse.replies.map((reply, key)=>{
        return(
          <div key={key}>
            <ReplyContainer
              reply={reply.fields}
            />
            <br/>
          </div>  
        )
      }):<div/>}
    </div>
  )

}

function Thread(){

  const [postreply, setPostReply] = useRecoilState(replyPostState);
  const [getcomment, setGetComment] = useRecoilState(commentGetState);
  const [commentgetresponse, setCommentGetResponse] = useRecoilState(commentGetResponse)
  const [currentBoard, setCurrentBoard] = useRecoilState(board)
  const [threadnum, setThreadnum] = useState('')
  const location = useLocation();

  useEffect(()=>{
    setThreadnum(location.pathname.replace("/"+currentBoard+"/", ''))
    setGetComment({id: location.pathname.replace("/"+currentBoard+"/", ""), submit: true})
  }, [])

  useEffect(()=>{
    console.log("the value of postreply is: ", postreply)
  }, [postreply])

  return(
    <div className='board'> 
      <div className='threadbanner'>
        Thread! {threadnum}  
      </div>
      <PostReplyContainer
        reply={postreply}
        submitReply={(e)=>{setPostReply({...e, ...{comment_id:threadnum}})}}
      />
      <br/>
      ~~~ Comment ~~~
      <br/>
      {commentgetresponse.comment.length!=0&&commentgetresponse.comment.fields!=undefined?
         <CommentContainer
           showthread={false}
           handleNavigate={()=>{}}
           comment={commentgetresponse.comment.fields}
         />:<div/>
      }
      <br/>
      ~~~ Replies ~~~
      <br/>
      <ReplyList />
    </div>
  )

}

export default Thread;