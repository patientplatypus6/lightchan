import React, { useEffect, useState } from 'react';
import '../main.css'


function PostCommentContainer({submitComment, comment}){

  const [title, setTitle] = useState("")
  const [content, setContent] = useState("")

  useEffect(()=>{
    console.log('inside postcommentcontainer and value of comment: ', comment)
    setContent(comment.content)
    setTitle(comment.title)
  }, [comment])

  const submitForm = () => {
    console.log('inside submitForm and value of title: ', title)
    console.log('inside submitForm and value of content: ', content)
    if(content==""){
      alert("Comment cannot be blank!")
      if(title==""){
        setTitle("no title")
      }
    }
    submitComment({title, content, submit: true})
  }

  return(
    <div className='submitcommentcontainer'>
      <input className='inputval' type="text" value={title} onChange={(e)=>{setTitle(e.target.value)}}></input>
      <br/>
      <textarea className='textval' type="text" value={content} onChange={(e)=>{setContent(e.target.value)}} />
      <br/>
      <div 
        className='submitcommentbutton'
        onClick={submitForm}>
        SUBMIT
      </div>
    </div>
  )
}

export default PostCommentContainer;