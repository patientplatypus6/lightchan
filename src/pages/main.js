
import React from 'react';
import {
  RecoilRoot,
  atom,
  selector,
  useRecoilState,
  useRecoilValue,
} from 'recoil';
// import {schema} from '../api/api'
import { testPost } from '../api/fetch';

import {
  textState, charCountState
} from '../state/state'

function CharacterCounter(){
  const [text, setText] = useRecoilState(textState);
  const onChange = (event) => {
    setText(event.target.value);
  };

  return(
    <div>
      <input type="text" value={text} onChange={onChange} />
      <br />
      Echo: {text}
    </div>
  )

}

function TestFetch(){

  testPost();

  return(
    <div>
      Inside the test of the fetch api.
    </div>
  )
}

//may implement later (why not just put in recoil?)
// function GraphSchema(){
//   return(
//     <div>
//       The value of the returning schema is - 
//       <div>
//         {JSON.stringify(schema)}
//       </div>
//     </div>
//   )
// }

function Main() {
  return (
    <div>
      <div>
        This is the main page.
      </div>
      <RecoilRoot>
        <CharacterCounter/> 
      </RecoilRoot>
      {/* <GraphSchema></GraphSchema> */}
      <TestFetch></TestFetch>
    </div>
  );
}

export default Main;
