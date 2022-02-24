import React, { useEffect, useState } from 'react';
import '../main.css'


function CommentContainer({comment, handleNavigate, showthread}){

  console.log('value of comment.image_path: ', comment.file_name)

  return(
    <div className='commentcontainer'>
      <div className='commenttitlebar'>
      <span style={{marginLeft: '10px'}}>{comment.created_at}</span><span style={{marginLeft: '10px'}}>{comment.title}</span>
      {showthread?<span className='viewbutton' onClick={()=>{
        handleNavigate()
      }}>view thread</span>:<span/>}
      </div>
      <div className='commentcontentbox'>
        {comment.file_name!=""&&comment.file_name!=undefined?<img src={"http://localhost:8000/static/"+comment.file_name}/>:<div/>}
        {comment.content}
      </div>
    </div>
  )
}

export default CommentContainer;