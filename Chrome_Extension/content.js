console.log('Initializing content script for Fakex');

let parasColored = false;

const toggleParagraphBG = (bgcolor) => {
  let ps = document.getElementsByTagName('p');

  if (parasColored) 
    bgcolor = 'transparent';

  for (p of ps) {
    p.style['background-color'] = bgcolor;
  }

  parasColored = !parasColored;
};

const gotMessage = (message, sender, sendResponse) => {
  console.log(message.txt);
  if (message.txt === 'hello') {
    toggleParagraphBG('#FF0000');
  }
};

chrome.runtime.onMessage.addListener(gotMessage);