
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


function CommentList(props){

  const [getcomment, setGetComment] = useRecoilState(commentGetState);
  const [commentgetresponse, setCommentGetResponse] = useRecoilState(commentGetResponse)
  const [postcomment, setPostComment] = useRecoilState(commentPostState);
  const [commentpostresponse, setCommentPostResponse] = useRecoilState(commentPostResponse);
  const [commentretrieveall, setCommentRetrieveAll] = useRecoilState(retrieveAllComments);

  const [dataArray, setDataArray] = useState([])

  useEffect(()=>{
    setDataArray(commentretrieveall.response.data)
  }, [commentretrieveall])    

  return( 
    <div style={{textAlign: 'center'}}>
      {dataArray!=undefined?dataArray.map((comment, key)=>{
        return(
          <div key={key}>
            <CommentContainer
              showthread={true}
              handleNavigate={()=>{
                props.handleNavigate('thread/'+comment.id)
              }}
              comment={comment}
            />
            <br/>
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
