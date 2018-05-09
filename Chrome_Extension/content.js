const url = 'https://fakex.herokuapp.com/api/';

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

const scoreNames = {
  fake: 'Fake',
  partiallyFake: 'Partially Fake',
  ambiguous: 'Ambiguous',
  partiallyVerified: 'Partially Verified',
  verified: 'Verified'
};

const errorBGColor = '#ff0000';

const gotMessage = (message, sender, sendResponse) => {

  const target = window.getSelection();
  const text = target.toString();
  const containerNode = target.anchorNode.parentNode;

  fetch(url + text)
    .then(response => response.json())
    .then(jsonData => {
      setBackgroundColor(containerNode, computeColorFromScore(jsonData.score), jsonData.score);
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
    return scoreColors.partiallyVerified;
  } else if (score > scoreThresholds.partiallyVerified && score < scoreThresholds.verified) {
    console.log('Verified');
    return scoreColors.verified;
  } else {
    console.log('Error');
    return errorBGColor;
  }
};

const getScoreName = (score) => {
  if (score < scoreThresholds.fake) {
    return scoreNames.fake;
  } else if (score > scoreThresholds.fake && score < scoreThresholds.partiallyFake) {
    return scoreNames.partiallyFake;
  } else if (score > scoreThresholds.partiallyFake && score < scoreThresholds.ambiguous) {
    return scoreNames.ambiguous;
  } else if (score > scoreThresholds.ambiguous && score < scoreThresholds.partiallyVerified) {
    return scoreNames.partiallyVerified;
  } else if (score > scoreThresholds.partiallyVerified && score < scoreThresholds.verified) {
    return scoreNames.verified;
  } else {
    return errorBGColor;
  }
};

const setBackgroundColor = (node, color, score) => {
  node.style.background = color;
  node.classList.add('fakex-target');


  let scoreNode = document.createElement('div');
  scoreNode.textContent = `${Math.round(score*100)}% - ${getScoreName(score)}`;
  scoreNode.style.backgroundColor = color;
  scoreNode.classList.add('fakex-score-container');
  node.appendChild(scoreNode);
};

chrome.runtime.onMessage.addListener(gotMessage);
