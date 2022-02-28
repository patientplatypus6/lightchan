

import React, {useEffect, useState} from 'react';

import {
  RecoilRoot,
  atom,
  selector,
  useRecoilState,
  useRecoilValue,
} from 'recoil';
// import {schema} from '../api/api'
import './main.css';

function Board(){
  return(
    <div className='wrapper'>
      <div className='nav'></div>
      <div className='board'></div>
      <div className='header'></div>
      <div className='stats'></div>
    </div>
  )
}

export default Board;