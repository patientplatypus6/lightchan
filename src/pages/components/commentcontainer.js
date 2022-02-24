import React, { useEffect, useState } from 'react';
import '../main.css'

import img404 from './img404.jpeg'

function CommentContainer({comment, handleNavigate, showthread}){

  const [imgError, setImgError] = useState(false)
  console.log('value of comment.image_path: ', comment.file_name)

  const pichandler=()=>{

    console.log('inside pichandler')

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
            src={"http://localhost:8000/static/"+comment.file_name} 
            className='commentimage'
          />
        )
      }
    }else{
      <div/>
    }

  }

  return(
    <div className='commentcontainer'>
      <div className='commenttitlebar'>
      <span style={{marginLeft: '10px'}}>{comment.created_at}</span><span style={{marginLeft: '10px'}}>{comment.title}</span>
      {showthread?<span className='viewbutton' onClick={()=>{
        handleNavigate()
      }}>view thread</span>:<span/>}
      </div>
      <div className='commentcontentbox'>
        {pichandler()}
        <div className='commentcontent'>
          {comment.content}
        </div>
      </div>
    </div>
  )
}

export default CommentContainer;