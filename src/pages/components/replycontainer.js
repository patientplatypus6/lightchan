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
        {reply.file_name!=""&&reply.file_name!=undefined?<img src={"http://localhost:8000/static/"+reply.file_name} className='replyimage'/>:<div/>}
        <div className='replycontent'>
          {reply.content}
        </div>
      </div>
    </div>
  )
}

export default ReplyContainer;