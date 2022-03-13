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
						<div className='boardlistitem' onClick={()=>{handleClick('man')}}>
							Main
						</div>
					</li>
					<li>
						<div className='boardlistitem' onClick={()=>{handleClick('mus')}}>
							Music
						</div>
					</li>
					<li>
						<div className='boardlistitem' onClick={()=>{handleClick('art')}}>
							Art
						</div>
					</li>
					<li>
						<div className='boardlistitem' onClick={()=>{handleClick('lit')}} >
							Literature
						</div>
					</li>
					<li>
						<div className='boardlistitem' onClick={()=>{handleClick('tec')}}>
							Technology
						</div>
					</li>
				</ul>
      </div>
    </div>
  )
}

export default Sidebar;