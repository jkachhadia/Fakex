const clicked = (tab) => chrome.tabs.sendMessage(tab.id, {});
chrome.browserAction.onClicked.addListener(clicked);