importScripts('https://www.gstatic.com/firebasejs/8.10.0/firebase-app.js');
importScripts('https://www.gstatic.com/firebasejs/8.10.0/firebase-messaging.js');

firebase.initializeApp({
    apiKey: 'AIzaSyALcJid507IJ6uVSCZBthQMi5GSNyMgL2g',
    authDomain: 'hrms-518c4.firebaseapp.com',
    projectId: 'hrms-518c4',
    storageBucket: 'hrms-518c4.appspot.com',
    messagingSenderId: '131244622426',
    appId: '1:131244622426:web:c2b4419b52ee473c524e63'
});

const messaging = firebase.messaging();

// Customize notification behavior here
messaging.setBackgroundMessageHandler(function (payload) {
  const notificationTitle = 'Background Message Title';
  const notificationOptions = {
    body: notificationTitle,
    icon: 'icon.png', // Replace with the path to your app's icon
  };

  return self.registration.showNotification(notificationTitle, notificationOptions);
});