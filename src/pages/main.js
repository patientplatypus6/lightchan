
import React, { useEffect, useState } from 'react';
import {
  RecoilRoot,
  atom,
  selector,
  useRecoilState,
  useRecoilValue,
} from 'recoil';
// import {schema} from '../api/api'
import Api from '../api/api';
import './main.css';

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
    console.log('value of data array: ', dataArray)
    if(dataArray!=undefined){
      console.log('value of data array at index 5: ', dataArray[5])
    }
  }, [dataArray])

  useEffect(()=>{
    console.log('inside useEffect in Comment to Retrieve all comments')
    console.log('value of retrieveall: ', commentretrieveall)
    setDataArray(commentretrieveall.response.data)
  }, [commentretrieveall])    

  return( 
    <div style={{textAlign: 'center'}}>
      {dataArray!=undefined?dataArray.map((comment, key)=>{
        return(
          <div key={key}>
            <div className='commentcontainer'>
              <div className='commenttitlebar'>
              <span style={{marginLeft: '10px'}}>{comment.created_at}</span><span style={{marginLeft: '10px'}}>{comment.title}</span>
              <span className='viewbutton' onClick={()=>{
                props.handleNavigate('thread/'+comment.id)
              }}>view thread</span>
              </div>
              <div className='commentcontentbox'>
                {comment.content}
              </div>
            </div>
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

  const onChangeComment = (event, name) => {
    if(name=='submit'&&postcomment.content==""){
      alert("Comment cannot be blank!")
    }else{
      if(name=="submit"&&postcomment.title==""){
        setPostComment({
          title: "no title", 
          content: name=="content"?event.target.value:postcomment.content,
          submit: name=="submit"?true:false
        })
      }else{
        setPostComment({
          title: name=="title"?event.target.value:postcomment.title, 
          content: name=="content"?event.target.value:postcomment.content,
          submit: name=="submit"?true:false
        })
      }
    }

  };


  return(
    <div style={{textAlign: 'center', width: '100vw'}}>
      <div className='welcomebanner'>
        Welcome To Lightchan!
      </div>
      <div className='submitcommentcontainer'>
        <input className='inputval' type="text" value={postcomment.title} onChange={(e)=>{onChangeComment(e, 'title')}}></input>
        <br/>
        <textarea className='textval' type="text" value={postcomment.content} onChange={(e)=>{onChangeComment(e, 'content')}} />
        <br/>
        <div 
          className='submitcommentbutton'
          onClick={()=>{onChangeComment("", "submit")}}>
          SUBMIT
        </div>
        <Api/>
      </div>
    </div>
  )

}

function Main(props) {
  return (
    <div className='main'>
      {/* <RecoilRoot> */}
        <Comment/> 
        <CommentList handleNavigate={props.handleNavigate}/>
      {/* </RecoilRoot> */}
    </div>
  );
}

export default Main;
