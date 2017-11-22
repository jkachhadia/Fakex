console.log('Running Background Script for Fakex');

const buttonClicked = (tab) => {
  let msg = {
    txt: "hello"
  };

  chrome.tabs.sendMessage(tab.id, msg);
};

chrome.browserAction.onClicked.addListener(buttonClicked);