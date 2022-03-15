import React, { useEffect, useState } from 'react';
import '../main.css'

import img404 from '../../images/img404.jpeg'
import arrow from '../../images/arrow.svg'

import {
  RecoilRoot,
  atom,
  selector,
  useRecoilState,
  useRecoilValue,
} from 'recoil';

import { voteField, voteData } from '../../state/state';
import { getCookie } from '../../utilities/utilities';


function ReplyContainer({reply}){

  const [vote, setVote] = useRecoilState(voteField);
  const [votedatum, setVoteData] = useRecoilState(voteData)

  console.log('inside replycontainer and value of reply: ', reply)

  const voteHandler=(direction)=>{
    console.log('^^**^^ inside voteHandler')
    console.log('^^**^^ value of reply inside votehandler', reply)
    var voteobj = {}
    if(direction=='up'){
      voteobj = {
        upvote: true, 
        downvote: false, 
        comment: false, 
        reply: true,
        id: reply.clean_id,
        submit: true
      }
    }else if(direction=='down'){
      voteobj = {
        upvote: false, 
        downvote: true, 
        comment: false, 
        reply: true,
        id: reply.clean_id,
        submit: true
      }
    }
    console.log('value of voteobj: ', voteobj)
    setVote(voteobj)
  }

  return(
    <div className='replycontainer'>
      <div className='replytitlebar'>
      <span style={{marginLeft: '10px'}}>{reply.created_at}</span><span style={{marginLeft: '10px'}}>{reply.title}</span>
      <span>
        {votedatum.votes[reply.clean_id]!=null?<div style={{display: 'inline-block', paddingLeft: '5p', paddingRight: '5px'}}>{votedatum.votes[reply.clean_id]}</div>:<div style={{display: 'inline-block', paddingLeft: '5px', paddingRight: '5px'}}>{reply.votes}</div>}
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
      <div className='replycontentbox'>
        {reply.file_name!=""&&reply.file_name!=undefined?<img src={"http://localhost:9000/static/"+reply.file_name} className='replyimage'/>:<div/>}
        <div className='replycontent'>
          {reply.content}
        </div>
      </div>
    </div>
  )
}

export default ReplyContainer;