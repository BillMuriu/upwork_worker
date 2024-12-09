var recorder_enabled = true;

var init = function () {
    // Load
    chrome.runtime.onInstalled.addListener(function (object) {
        chrome.notifications.create("T_" + Date.now(), {
            type: 'basic',
            iconUrl: 'images/recorder_icon.png',
            title: 'SeleniumBase Recorder ACTIVE',
            message: '[ESC]: Pause recording.\n[~`]: Resume recording.',
            priority: 2
        });
    });
    // User clicks icon
    chrome.browserAction.onClicked.addListener(function (tab) {
        chrome.notifications.create("T_" + Date.now(), {
            type: 'basic',
            iconUrl: 'images/recorder_icon.png',
            title: 'SeleniumBase Recorder ACTIVE',
            message: '[ESC]: Pause recording.\n[~`]: Resume recording.',
            priority: 2
        });
        //chrome.tabs.create({url: "https://seleniumbase.io"}, function (tab) {
        //});
    });
    // User opens url
    chrome.webNavigation.onCompleted.addListener(function (details) {
    });
    // User changes tab
    chrome.tabs.onActivated.addListener(function (activeInfo) {
    });
};
init();
