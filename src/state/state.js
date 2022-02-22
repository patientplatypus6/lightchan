import React from 'react';

import {
  RecoilRoot,
  atom,
  selector,
  useRecoilState,
  useRecoilValue,
} from 'recoil';

const commentState = atom({  
  key: 'commentState',
  default: {title: "", content: "", submit: false}
})

const commentPostResponse = atom({  
  key: 'commentPostResponse',
  default: {response: {}}
})

export {commentState, commentPostResponse}