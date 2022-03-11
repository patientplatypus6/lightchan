import React, { useEffect, useState } from 'react';
import '../main.css'

import img404 from '../../images/img404.jpeg'
import arrow from '../../images/arrow.svg'


function ReplyContainer({reply}){

  console.log('inside replycontainer and value of reply: ', reply)

  return(
    <div className='replycontainer'>
      <div className='replytitlebar'>
      <span style={{marginLeft: '10px'}}>{reply.created_at}</span><span style={{marginLeft: '10px'}}>{reply.title}</span>
      <span>
        <div className='arrowbutton'>
          <img style={{height: '100%'}} src={arrow}/>
        </div>
      </span>
      <span>
        <div className='arrowbutton'>
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