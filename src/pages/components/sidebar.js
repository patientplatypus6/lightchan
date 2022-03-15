import React, {useEffect, useState} from 'react';
import '../main.css'

import {
  RecoilRoot,
  atom,
  selector,
  useRecoilState,
  useRecoilValue,
} from 'recoil';
import { board, boards, displayBoard, currentBoardSel, retrieveAllComments } from '../../state/state';

function Sidebar(props){

	const [boardsData, setBoardsData] = useRecoilState(boards);
	const [currentBoard, setCurrentBoard] = useRecoilState(board);
	const [commentretrieveall, setCommentRetrieveAll] = useRecoilState(retrieveAllComments);

	const [showDisplayBoard, setDisplayBoard] = useState("main")

	const selectorCurrentBoard  = useRecoilState(currentBoardSel)

  console.log("inside the sidebar!")

	const handleClick = (nme) => {
		setCurrentBoard(nme)
		props.handleNavigate(nme)
	}

	useEffect(()=>{
		setBoardsData({submit: true, response: null})
	}, [])

  return( 
    <div className='nav'>
      <div className='sidebar'>
				CurrentBoard <span style={{fontWeight: 'bold'}}>{currentBoard}</span>
					{boardsData['response']!=null?
						<ul className='boards'>
							{boardsData['response'].map((board, key)=>{
								const boardname = board["mnemonic"]
								console.log("value of board in loop: ", board)
								return(
									<li key={key}>
										<div className='boardlistitem' onClick={()=>{handleClick(boardname)}}>
											{board.board_name}
										</div>
									</li>
								)
							})}
						</ul>
					:<div/>}
      </div>
    </div>
  )
}

export default Sidebar;