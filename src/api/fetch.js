
import React from 'react';

var testPost = async () => {
  return fetch('http://localhost:8090/testpost', { mode: 'cors' }) 
  .then(response => response.json())
  .then(data => console.log(data));
} 

export {testPost}