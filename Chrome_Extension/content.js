const url = 'http://fakex.herokuapp.com/api/';

const scoreColors = {
  fake: '#FF9800',
  partiallyFake: '#FFC107',
  ambiguous: '#FFEB3B',
  partiallyVerified: '#CDDC39',
  verified: '#8BC34A'
};

const scoreThresholds = {
  fake: 0.6,
  partiallyFake: 0.6633,
  ambiguous: 0.7266,
  partiallyVerified: 8,
  verified: 1
};

const errorBGColor = '#000';

const gotMessage = (message, sender, sendResponse) => {

  const target = window.getSelection();
  const text = target.toString();
  const containerNode = target.anchorNode.parentNode;

  fetch(url + text)
    .then(response => response.json())
    .then(jsonData => {
      setBackgroundColor(containerNode, computeColorFromScore(jsonData.score));
    });
};

// score ranges from 0 to 1
const computeColorFromScore = (score) => {
  if (score < scoreThresholds.fake) {
    console.log('Fake');
    return scoreColors.fake;
  } else if (score > scoreThresholds.fake && score < scoreThresholds.partiallyFake) {
    console.log('Partially fake');
    return scoreColors.partiallyFake;
  } else if (score > scoreThresholds.partiallyFake && score < scoreThresholds.ambiguous) {
    console.log('Ambiguous');
    return scoreColors.ambiguous;
  } else if (score > scoreThresholds.ambiguous && score < scoreThresholds.partiallyVerified) {
    console.log('Partially Verified');
    return scoreThresholds.partiallyVerified;
  } else if (score > scoreThresholds.partiallyVerified && score < scoreThresholds.verified) {
    console.log('Verified');
    return scoreColors.verified;
  } else {
    console.log('Error');
    return errorBGColor;
  }

};

const setBackgroundColor = (node, color) => {
  node.style.background = color;
};

chrome.runtime.onMessage.addListener(gotMessage);
