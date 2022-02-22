
import React, { useEffect } from 'react';
import {
  RecoilRoot,
  atom,
  selector,
  useRecoilState,
  useRecoilValue,
} from 'recoil';
// import {schema} from '../api/api'
import axios from 'axios';
import { testPost } from '../api/fetch';

import {
  commentState, commentPostResponse
} from '../state/state'

function Api({name}){
  const [comment, setComment] = useRecoilState(commentState);
  const [response, setResponse] = useRecoilState(commentPostResponse);

  useEffect(()=>{
    console.log("inside Api and value of name: ", name)
    console.log("useEffect of Api and value of comment: ", comment)
    if(name=='comment' && comment.submit){
      axios.post(
        "http://localhost:8000/lightone/comment/1/", 
        {title: comment.title, content: comment.content}
      )
      .then(response=>{
        console.log("*************************************")
        console.log("here is the response: ", response)
        console.log("*************************************")
        setResponse({response});
        setComment({title: '', content: '', submit: false})
      })
      .catch(response=>{
        console.log("*************************************")
        console.log('there was an error: ', response)
        console.log("*************************************")
        setResponse({response});
        setComment({title: '', content: '', submit: false})
      })
    }
  }, [comment])
  
  return(
    <div></div>
  )

}

export default Api;
