
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
  commentGetState, 
  commentGetResponse,  commentPostState, commentPostResponse, retrieveAllComments
} from '../state/state'

function Api(){
  const [getcomment, setGetComment] = useRecoilState(commentGetState);
  const [commentgetresponse, setCommentGetResponse] = useRecoilState(commentGetResponse)
  const [postcomment, setPostComment] = useRecoilState(commentPostState);
  const [commentpostresponse, setCommentPostResponse] = useRecoilState(commentPostResponse);
  const [commentretrieveall, setCommentRetrieveAll] = useRecoilState(retrieveAllComments);

  useEffect(()=>{
    // console.log("inside Api and value of name: ", name)
    // console.log("useEffect of Api and value of comment: ", comment)
    if(postcomment.submit){
      axios.post(
        "http://localhost:8000/lightone/comment/1/", 
        {title: postcomment.title, content: postcomment.content}
      )
      .then(response=>{
        // console.log("*************************************")
        // console.log("here is the response: ", response)
        // console.log("*************************************")
        setCommentPostResponse({response});
        setPostComment({title: '', content: '', submit: false})
      })
      .catch(response=>{
        // console.log("*************************************")
        // console.log('there was an error: ', response)
        // console.log("*************************************")
        setCommentPostResponse({response});
        setPostComment({title: '', content: '', submit: false})
      })
    }
  }, [postcomment])

  useEffect(()=>{ 
    if(getcomment.submit && getcomment.id!=""){
      axios.get(
        "http://localhost:8000/lightone/comment/"+getcomment.id
      )
      .then(response=>{
        // console.log("*************************************")
        // console.log("here is the response: ", response)
        // console.log("*************************************")
        setCommentGetResponse({response});
        setGetComment({id: '', submit: false})
      })
      .catch(response=>{
        // console.log("*************************************")
        // console.log('there was an error: ', response)
        // console.log("*************************************")
        setCommentGetResponse({response});
        setGetComment({id: '', submit: false})  
      })
    }
  }, [getcomment])

  useEffect(()=>{
    if(commentretrieveall.submit){
      axios.get(
        "http://localhost:8000/lightone/comments/"
      )
      .then(response=>{
        console.log("*************************************")
        console.log("here is the response: ", response)
        console.log("*************************************")
        setCommentRetrieveAll({submit: false, response});
      })
      .catch(response=>{
        console.log("*************************************")
        console.log('there was an error: ', response)
        console.log("*************************************")
        setCommentRetrieveAll({submit: false, response});
      })
    }
  }, [commentretrieveall])
  
  return(
    <div></div>
  )

}

export default Api;
