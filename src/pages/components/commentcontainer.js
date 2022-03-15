import React, { useEffect, useState } from 'react';
import '../main.css'

import img404 from '../../images/img404.jpeg'
import arrow from '../../images/arrow.svg'

import { voteField, voteData } from '../../state/state';
import { getCookie } from '../../utilities/utilities';

import {
  RecoilRoot,
  atom,
  selector,
  useRecoilState,
  useRecoilValue,
} from 'recoil';

function CommentContainer({comment, handleNavigate, showthread}){

  const [imgError, setImgError] = useState(false)
  const [votedatum, setVoteData] = useRecoilState(voteData)
  const [vote, setVote] = useRecoilState(voteField);

  console.log('value of comment.image_path: ', comment.file_name)

  const voteHandler=(direction)=>{
    console.log('inside voteHandler')
    var voteobj = {}
    if(direction=='up'){
      voteobj = {
        upvote: true, 
        downvote: false, 
        comment: true, 
        reply: false,
        id: comment.clean_id,
        submit: true
      }
    }else if(direction=='down'){
      voteobj = {
        upvote: false, 
        downvote: true, 
        comment: true, 
        reply: false,
        id: comment.clean_id,
        submit: true
      }
    }
    console.log('value of voteobj: ', voteobj)
    setVote(voteobj)

  }

  const picHandler=()=>{

    console.log('inside picHandler')
    console.log('value of comment : ', comment)

    if(comment.file_name!=""&&comment.file_name!=undefined){
      if(imgError){
        return(
          <img
            src={img404} 
            className='commentimage'
          />
        )
      }else{
        return(
          <img
            onError={()=>{
              console.log("inside the onError function")
              setImgError(true)
            }}
            src={"http://localhost:9000/static/"+comment.file_name} 
            className='commentimage'
          />
        )
      }
    }else{
      <div/>
    }

  }

  useEffect(()=>{
    console.log("VALUE OF COOKIES: ", document.cookie.toString())
  })

  return(
    <div className='commentcontainer'>
      <div className='commenttitlebar'>
      <span style={{marginLeft: '10px'}}>{comment.created_at}</span><span style={{marginLeft: '10px'}}>{comment.title}</span>
      {showthread?<span className='viewbutton' onClick={()=>{
        handleNavigate()
      }}>view thread</span>:<span/>}
      <span>
        {votedatum.votes[comment.clean_id]!=null?<div style={{display: 'inline-block', paddingLeft: '5p', paddingRight: '5px'}}>{votedatum.votes[comment.clean_id]}</div>:<div style={{display: 'inline-block', paddingLeft: '5px', paddingRight: '5px'}}>{comment.votes}</div>}
      </span>
      <span>
        <div className='arrowbutton'
          onClick={()=>{voteHandler('up')}}
        >
          <img style={{height: '100%'}} src={arrow}/>
        </div>
      </span>
      <span>
        <div className='arrowbutton'
          onClick={()=>{voteHandler('down')}}
        >
          <img style={{height: '100%', transform: 'rotate(180deg)'}} src={arrow}/>
        </div>
      </span>
      </div>
      <div className='commentcontentbox'>
        {picHandler()}
        <div className='commentcontent'>
          {comment.content}
        </div>
      </div>
    </div>
  )
}

export default CommentContainer;