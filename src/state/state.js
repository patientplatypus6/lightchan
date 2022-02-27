import React from 'react';

import {
  RecoilRoot,
  atom,
  selector,
  useRecoilState,
  useRecoilValue,
} from 'recoil';

//vote / setVote
const voteField = atom({
  key: 'voteField',
  default: {
    upvote: false, 
    downvote: false, 
    comment: false, 
    reply: false,
    id: "",
    submit: false
  }
})

//votedatum / setVoteData
const voteData = atom({
  key: 'voteData', 
  default: {votes: {}}
})

//uploadfile / setUploadFile
const uploadFile = atom({
  key: 'uploadFile',
  default: null
})

//postreply / setPostReply
const replyPostState = atom({  
  key: 'replyPostState',
  default: {title: "", content: "", comment_id: "", submit: false}
})

//getreply / setGetReply
const replyGetState = atom({  
  key: 'replyGetState',
  default: {id: "", submit: false}
})

//replygetresponse / setReplyGetResponse
const replyGetResponse = atom({  
  key: 'replyGetResponse',
  default: {response: {}}
})

//don't end up using
//replypostresponse / setReplyPostResponse
const replyPostResponse = atom({  
  key: 'replyPostResponse',
  default: {response: {}}
})

//commentretrieveall / setCommentRetrieveAll
const retrieveAllRepliesByID = atom({  
  key: 'retrieveAllRepliesByID',
  default: {submit: false, comment_id: "", response: {}}
})

//postcomment / setPostComment
const commentPostState = atom({  
  key: 'commentPostState',
  default: {title: "", content: "", submit: false}
})

//getcomment / setGetComment
const commentGetState = atom({  
  key: 'commentGetState',
  default: {id: "", submit: false}
})

//commentgetresponse / setCommentGetResponse
const commentGetResponse = atom({  
  key: 'commentGetResponse',
  default: {comment: {}, replies: []}
})

//commentpostresponse / setCommentPostResponse
const commentPostResponse = atom({  
  key: 'commentPostResponse',
  default: {response: {}}
})

//commentretrieveall / setCommentRetrieveAll
const retrieveAllComments = atom({  
  key: 'retrieveAllComments',
  default: {submit: false, response: {}}
})

export {
  voteField,
  voteData,
  uploadFile,
  replyGetState, 
  replyGetResponse,
  replyPostState,
  replyPostResponse,
  retrieveAllRepliesByID,
  commentPostState, 
  commentPostResponse,   
  commentGetState, 
  commentGetResponse, 
  retrieveAllComments,
}