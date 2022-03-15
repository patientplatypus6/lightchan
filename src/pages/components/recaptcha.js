import React, { render, useRef, useEffect } from "react"

import ReCAPTCHA from "react-google-recaptcha";

import { captcha } from "../../state/state";

import {
  useRecoilState
} from 'recoil';

import {
	commentPostState,
	replyPostState
} from '../../state/state'

function Recaptcha(props){
	const [postcomment, setPostComment] = useRecoilState(commentPostState);
	const [postreply, setPostReply] = useRecoilState(replyPostState);
	const [captchaValue, setCaptchaValue] = useRecoilState(captcha);
	const recaptcharef = useRef(null);

	useEffect(()=>{
		if(postcomment.submit || postreply.submit){
			recaptcharef.current.reset()
		}
	}, [postcomment, postreply])

	function onChange(value) {
		console.log("Captcha value:", value);
		setCaptchaValue(value);
	}

	return(
		<ReCAPTCHA
			ref={recaptcharef}
			style={{display: 'inline-block'}}
			sitekey={process.env.REACT_APP_RECAPTCHA_KEY}
			onChange={onChange}
			theme='dark'
		/>
	)
}

export default Recaptcha