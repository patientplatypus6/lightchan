
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
import { board } from '../state/state';
import {
  commentGetState, 
  commentGetResponse,  commentPostState, commentPostResponse, retrieveAllComments
} from '../state/state'
import ReplyContainer from './components/replycontainer';


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
                props.handleNavigate(+cr.comment.fields.clean_id)
              }}
              comment={currentBoard + '/' + cr.comment.fields}
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

function Comment(){

  const [getcomment, setGetComment] = useRecoilState(commentGetState);
  const [commentgetresponse, setCommentGetResponse] = useRecoilState(commentGetResponse)
  const [postcomment, setPostComment] = useRecoilState(commentPostState);
  const [commentpostresponse, setCommentPostResponse] = useRecoilState(commentPostResponse);
  const [commentretrieveall, setCommentRetrieveAll] = useRecoilState(retrieveAllComments);

  const retrieveComments = () => {
    console.log('inside set retrieve Comments')
    setCommentRetrieveAll({
      submit: true,
      response: {}
    })
  }

  useEffect(()=>{
    console.log('inside useEffect in Comment to Retrieve all comments')
    retrieveComments()
  }, [])  

  useEffect(()=>{
    console.log("useEffect of Comment and comment: ", postcomment)
  }, [postcomment])

  useEffect(()=>{
    retrieveComments()
  }, [commentpostresponse])

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
  return (
    <div className='board'>
      <Comment/> 
      <CommentList handleNavigate={props.handleNavigate}/>
    </div>
  );
}

export default Main;
