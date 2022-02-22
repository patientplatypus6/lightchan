
import React, { useEffect } from 'react';
import {
  RecoilRoot,
  atom,
  selector,
  useRecoilState,
  useRecoilValue,
} from 'recoil';
// import {schema} from '../api/api'
import Api from '../api/api';

import {
  commentPostResponse,
  commentState
} from '../state/state'

function Comment(){

  const [comment, setComment] = useRecoilState(commentState);
  const [response, setResponse] = useRecoilState(commentPostResponse);
  // const submit = useRecoilValue(submitComment);

  useEffect(()=>{
    console.log("useEffect of Comment and comment: ", comment)
  }, [comment])

  useEffect(()=>{
    console.log("useEffect of Comment and comment post response: ", response)
  }, [response])


  const onChangeComment = (event, name) => {
    console.log("inside onChangeComment and value of event: ", event)
    console.log("inside onChangeComment and value of name: ", name)
    setComment({
      title: name=="title"?event.target.value:comment.title, 
      content: name=="content"?event.target.value:comment.content,
      submit: name=="submit"?true:false
    })

  };


  return(
    <div>
      <div>
        Comment: 
      </div>
      <div>
        <input type="text" value={comment.title} onChange={(e)=>{onChangeComment(e, 'title')}}></input>
        <br/>
        <textarea type="text" value={comment.content} onChange={(e)=>{onChangeComment(e, 'content')}} />
        <br/>
        <div 
          style={{
            display: 'inline-block',
            paddingTop: '5px',
            cursor: 'pointer', background: 'blue', color: 'white', padding: '5px'}}
          onClick={()=>{onChangeComment("", "submit")}}>
          SUBMIT
        </div>
        <Api name="comment"/>
      </div>
    </div>
  )

}

function Main() {
  return (
    <div>
      <div>
        This is the main page.
      </div>
      <RecoilRoot>
        <Comment/> 
      </RecoilRoot>
    </div>
  );
}

export default Main;
