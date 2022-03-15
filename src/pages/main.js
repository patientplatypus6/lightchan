
import React, { useEffect, useState } from 'react';
import {
  RecoilRoot,
  atom,
  selector,
  useRecoilState,
  useRecoilValue,
} from 'recoil';
// import {schema} from '../api/api'
import './main.css';
import CommentContainer from './components/commentcontainer';
import PostCommentContainer from './components/postcommentcontainer';
import {
  commentGetState, 
  boards, board,
  commentGetResponse,  commentPostState, 
  commentPostResponse, retrieveAllComments
} from '../state/state'
import ReplyContainer from './components/replycontainer';

import {
  useLocation
} from 'react-router-dom';

function CommentList(props){

  const [commentretrieveall, setCommentRetrieveAll] = useRecoilState(retrieveAllComments);
  const [currentBoard, setCurrentBoard] = useRecoilState(board)

  useEffect(()=>{
    console.log("*************")
    console.log("*************")
    console.log("*************")

    console.log('value of commentretrieveall: ', commentretrieveall)

    console.log("*************")
    console.log("*************")
    console.log("*************")
    
  }, [commentretrieveall])    

  return( 
    <div style={{textAlign: 'center'}}>
      {commentretrieveall.response.data!=undefined?commentretrieveall.response.data.map((cr, key)=>{
        return(
          <div key={key}>
            <CommentContainer
              showthread={true}
              handleNavigate={()=>{
                props.handleNavigate(currentBoard + "/" + cr.comment.fields.clean_id)
              }}
              comment={cr.comment.fields}
            />
            <br/>
            <div style={{marginLeft: '5vw'}}>
            {cr.replies.length>0?cr.replies.map((reply, keyreplies)=>{
              return(
                <div key={keyreplies}>
                <ReplyContainer
                  reply={reply.fields}
                />  
                </div>
              )
            }):<div/>}
            </div>
          </div>  
        )
      }):<div/>}
    </div>
  )

}

function Comment(props){

  const [getcomment, setGetComment] = useRecoilState(commentGetState);
  const [commentgetresponse, setCommentGetResponse] = useRecoilState(commentGetResponse)
  const [postcomment, setPostComment] = useRecoilState(commentPostState);
  const [commentpostresponse, setCommentPostResponse] = useRecoilState(commentPostResponse);
  const [commentretrieveall, setCommentRetrieveAll] = useRecoilState(retrieveAllComments);
	const [boardsData, setBoardsData] = useRecoilState(boards);

  useEffect(()=>{
    console.log("useEffect of Comment and comment: ", postcomment)
  }, [postcomment])

  useEffect(()=>{
    props.retrieveComments()
  }, [commentpostresponse])

  useEffect(()=>{
    console.log('value of props: ', props)
  }, [props])

  return(
    <div>
      <PostCommentContainer
        comment={postcomment}
        submitComment={(e)=>{setPostComment(e)}}
      />
    </div>
  )
}

function Main(props) {

  const location = useLocation();
  const [currentBoard, setCurrentBoard] = useRecoilState(board)

  useEffect(()=>{
    setCurrentBoard(location.pathname.replace("/", ""))
  }, [])

  return (
    <div className='board'>
      <Comment retrieveComments={props.retrieveComments} /> 
      <CommentList handleNavigate={props.handleNavigate}/>
    </div>
  );
}

export default Main;
