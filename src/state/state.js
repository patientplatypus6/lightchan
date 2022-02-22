import React from 'react';

import {
  RecoilRoot,
  atom,
  selector,
  useRecoilState,
  useRecoilValue,
} from 'recoil';

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
  key: 'commentPostResponse',
  default: {response: {}}
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
  commentPostState, 
  commentPostResponse,   
  commentGetState, 
  commentGetResponse, 
  retrieveAllComments,
}