
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
  commentGetResponse,  commentPostState, commentPostResponse, retrieveAllComments
} from '../state/state'
import ReplyContainer from './components/replycontainer';


function CommentList(props){

  const [commentretrieveall, setCommentRetrieveAll] = useRecoilState(retrieveAllComments);
  // const [dataArray, setDataArray] = useState([])

  useEffect(()=>{
    // setDataArray(commentretrieveall.response.data)
    console.log('value of commentretrieveall: ', commentretrieveall)
  }, [commentretrieveall])    

  return( 
    <div style={{textAlign: 'center'}}>
      {commentretrieveall.response.data!=undefined?commentretrieveall.response.data.map((cr, key)=>{
        return(
          <div key={key}>
            <CommentContainer
              showthread={true}
              handleNavigate={()=>{
                props.handleNavigate('thread/'+cr.comment.fields.clean_id)
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
      }):<div>Some error</div>}
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
    <div style={{textAlign: 'center', width: '100vw'}}>
      <div className='welcomebanner'>
        Welcome To Lightchan!
      </div>
      <PostCommentContainer
        comment={postcomment}
        submitComment={(e)=>{setPostComment(e)}}
      />
    </div>
  )
}

function Main(props) {
  return (
    <div className='main'>
      <Comment/> 
      <CommentList handleNavigate={props.handleNavigate}/>
    </div>
  );
}

export default Main;
