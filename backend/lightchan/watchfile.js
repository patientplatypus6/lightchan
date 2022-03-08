console.log('INSIDE NODE EVENT FILE WATCH HANDLER')

const fs = require('fs');

const watcher = async () =>{
    console.log('inside async file watcher')
    fs.watch(".", (eventType, filename) => {
        console.log("the . directory was modified");
      });
}

watcher()