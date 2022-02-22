import React, { useEffect, useState } from 'react';
import '../main.css'


function ReplyContainer({reply}){

  console.log('inside replycontainer and value of reply: ', reply)

  return(
    <div className='replycontainer'>
      <div className='replytitlebar'>
      <span style={{marginLeft: '10px'}}>{reply.created_at}</span><span style={{marginLeft: '10px'}}>{reply.title}</span>
      </div>
      <div className='replycontentbox'>
        {reply.content}
      </div>
    </div>
  )
}

export default ReplyContainer;