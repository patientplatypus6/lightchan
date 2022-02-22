import React, { useEffect, useState } from 'react';
import '../main.css'


function CommentContainer({comment, handleNavigate, showthread}){

  return(
    <div className='commentcontainer'>
      <div className='commenttitlebar'>
      <span style={{marginLeft: '10px'}}>{comment.created_at}</span><span style={{marginLeft: '10px'}}>{comment.title}</span>
      {showthread?<span className='viewbutton' onClick={()=>{
        handleNavigate()
      }}>view thread</span>:<span/>}
      </div>
      <div className='commentcontentbox'>
        {comment.content}
      </div>
    </div>
  )
}

export default CommentContainer;