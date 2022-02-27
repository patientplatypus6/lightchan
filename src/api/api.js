
import React, { useEffect, useState } from 'react';
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

import { getCookie } from '../utilities/utilities';

import {
  uploadFile,
  replyGetState, 
  replyPostState,
  replyGetResponse, 
  replyPostResponse,
  retrieveAllRepliesByID,
  commentGetState, 
  commentGetResponse,  
  commentPostState, 
  commentPostResponse, 
  retrieveAllComments, 
  voteField, 
  voteData
} from '../state/state'

function Api(){

  const [vote, setVote] = useRecoilState(voteField)
  const [votedatum, setVoteData] = useRecoilState(voteData)
  const [uploadfile, setUploadFile] = useRecoilState(uploadFile);
  const [getreply, setGetReply] = useRecoilState(replyGetState);
  const [postreply, setPostReply] = useRecoilState(replyPostState);
  const [replypostresponse, setReplyPostResponse] = useRecoilState(replyPostResponse);
  const [replygetresponse, setReplyGetResponse] = useRecoilState(replyGetResponse);
  const [getcomment, setGetComment] = useRecoilState(commentGetState);
  const [commentgetresponse, setCommentGetResponse] = useRecoilState(commentGetResponse)
  const [postcomment, setPostComment] = useRecoilState(commentPostState);
  const [commentpostresponse, setCommentPostResponse] = useRecoilState(commentPostResponse);
  const [commentretrieveall, setCommentRetrieveAll] = useRecoilState(retrieveAllComments);
  const [replyretrieveallbyid, setReplyRetrieveAllByID] = useRecoilState(retrieveAllRepliesByID);

  useEffect(()=>{
    axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
    axios.defaults.xsrfCookieName = "csrftoken";
    axios.defaults.withCredentials= true;
    axios.defaults.headers.common['X-CSRFTOKEN']=getCookie('csrftoken');    
  }, [])

  const createUploadForm = (kind) => {

    console.log('value of uploadFile: ', uploadfile)

    var formData = new FormData();
    formData.append("image", uploadfile)
    setUploadFile(null)
    var obj = {}
    if(kind=='comment'){
      obj = {title: postcomment.title, content: postcomment.content}
    }else if(kind=='reply'){
      obj = {title: postreply.title, content: postreply.content, comment_id: postreply.comment_id}
    }
    const json = JSON.stringify(obj);
    const blob = new Blob([json], {
      type: 'application/json'
    });
    formData.append("document", blob);
    return formData
  }

  useEffect(()=>{

    //might need this: https://stackoverflow.com/questions/47874659/making-an-axios-post-request-with-multipart-form-data-via-react-native-debugger

    if(postcomment.submit){
      var formdata = createUploadForm('comment')
      console.log('value of formdata: ', formdata)
      var document = formdata.get('document')
      console.log('value of document: ', document)
      var image = formdata.get('image')
      console.log('value of image: ', image)
      axios.post(
        "http://localhost:8000/lightone/comment/1/", 
        formdata
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
    console.log("inside getcomment effect")
    console.log('value of getcomment in api: ', getcomment)
    if(getcomment.submit && getcomment.id!=""){
      axios.get(
        "http://localhost:8000/lightone/comment/"+getcomment.id+"/"
      )
      .then(response=>{
        setCommentGetResponse({
          comment: response.data.comment, 
          replies: response.data.replies
        });
        setGetComment({id: '', submit: false})
      })
      .catch(response=>{
        // console.log("*************************************")
        // console.log('there was an error: ', response)
        // console.log("*************************************")
        setCommentGetResponse({comment: {}, replies: []});
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
        // console.log("*************************************")
        // console.log("here is the response: ", response)
        // console.log("*************************************")
        setCommentRetrieveAll({submit: false, response});
      })
      .catch(response=>{
        // console.log("*************************************")
        // console.log('there was an error: ', response)
        // console.log("*************************************")
        setCommentRetrieveAll({submit: false, response});
      })
    }
  }, [commentretrieveall])

  useEffect(()=>{
    if(postreply.submit){
      var formdata = createUploadForm('reply')
      axios.post(
        "http://localhost:8000/lightone/reply/"+postreply.comment_id+"/", 
        formdata
      )
      .then(response=>{
        // console.log("*************************************")
        // console.log("here is the response: ", response)
        // console.log("*************************************")
        setCommentGetResponse({
          comment: response.data.comment, 
          replies: response.data.replies
        });
        setPostReply({title: "", content: "", comment_id: "", submit:false})
      })
      .catch(response=>{
        // console.log("*************************************")
        // console.log('there was an error: ', response)
        // console.log("*************************************")
        setPostReply({title: "", content: "", comment_id: "", submit:false})
      })
    }
  }, [postreply])

  useEffect(()=>{
    if(replyretrieveallbyid.submit){
      var comment_id = replyretrieveallbyid.comment_id
      axios.get(
        "http://localhost:8000/lightone/replies/"+replyretrieveallbyid.comment_id+"/"
      )
      .then(response=>{
        // console.log("*************************************")
        // console.log("here is the response: ", response)
        // console.log("*************************************")
        setReplyRetrieveAllByID({submit: false, comment_id, response})
      })
      .catch(response=>{
        // console.log("*************************************")
        // console.log('there was an error: ', response)
        // console.log("*************************************")
        setReplyRetrieveAllByID({submit: false, comment_id, response})
      })
    }
  }, [replyretrieveallbyid])


  useEffect(()=>{
    console.log('inside voteField')
    console.log('value of vote: ', vote)
    var downvote = vote.downvote
    var upvote = vote.upvote
    if(vote.submit){
      if(vote.comment==true){
        var url = "http://localhost:8000/lightone/comment/"+vote.id+"/"
      }else if(vote.reply==true){
        var url = "http://localhost:8000/lightone/reply/"+vote.id+"/"
      }
      axios.put(
        url,
        {upvote, downvote}
      )
      .then(response=>{
        console.log("*************************************")
        console.log("here is the response: ", response)
        console.log("*************************************")
        var votes = Object.assign({}, votedatum.votes)
        var voteindex = vote.id.toString()
        votes[voteindex] = response.data.votes
        
        setVoteData({votes})

        setVote({
          upvote: false, 
          downvote: false, 
          comment: false, 
          reply: false,
          id: "",
          submit: false
        })

      })
      .catch(response=>{
        // console.log("*************************************")
        // console.log('there was an error: ', response)
        // console.log("*************************************")

        setVote({
          upvote: false, 
          downvote: false, 
          comment: false, 
          reply: false,
          id: "",
          submit: false
        })

      })
    }
  }, [vote])
  
  return(
    <div></div>
  )

}

export default Api;
