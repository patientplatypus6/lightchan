import React, {useEffect, useState} from 'react';
import '../main.css'

import {
  RecoilRoot,
  atom,
  selector,
  useRecoilState,
  useRecoilValue,
} from 'recoil';
import { board } from '../../state/state';

function Sidebar(){

	const [currentBoard, setCurrentBoard] = useRecoilState(board);

  console.log("inside the sidebar!")

	const handleClick = (nme) => {
		setCurrentBoard(nme)
	}

  return( 
    <div className='nav'>
      <div className='sidebar'>
				CurrentBoard <span style={{fontWeight: 'bold'}}>{currentBoard}</span>
				<ul className='boards'>
					<li>
						<div className='boardlistitem' onClick={()=>{handleClick('main')}}>
							Main
						</div>
					</li>
					<li>
						<div className='boardlistitem' onClick={()=>{handleClick('board1')}}>
								Board 1
						</div>
					</li>
					<li>
						<div className='boardlistitem' onClick={()=>{handleClick('board2')}}>
							Board 2
						</div>
					</li>
					<li>
						<div className='boardlistitem' onClick={()=>{handleClick('board3')}} >
							Board 3
						</div>
					</li>
					<li>
						<div className='boardlistitem' onClick={()=>{handleClick('board4')}}>
							Board 4
						</div>
					</li>
				</ul>
      </div>
    </div>
  )
}

export default Sidebar;