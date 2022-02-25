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
      }):<div/>}
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
    console.log("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
    console.log('inside commentgetresponse and value of response: ', commentgetresponse)
    console.log("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
    console.log('commentgetresponse.comment.fields', commentgetresponse.comment.fields)
  }, [commentgetresponse])

  useEffect(()=>{
    setThreadnum(location.pathname.replace('/thread/', ''))
    setGetComment({id: location.pathname.replace("/thread/", ""), submit: true})
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
      {commentgetresponse.replies!=[]?
        <ReplyList 
          replies={
            commentgetresponse.replies
          }
        />
      :<div/>}
    </div>
  )

}

export default Thread;