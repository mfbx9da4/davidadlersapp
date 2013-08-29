/*
export PATH=$PATH:/home/david/Dropbox/Programming/Python/Miscellaneous/extensions/google_appengine
dev_appserver.py helloworld/
appcfg.py update helloworld/
*/

    //var website = 'http://davidadlersapp.appspot.com/';
    //var fbsecr = '244b438e67524756fcdaedb24a54e8c5';

  var fbid = '287745697930531';
window.fbAsyncInit = function() {
    // init the FB JS SDK
    FB.init({
      appId      : fbid, // App ID from the App Dashboard
      status     : true, // check the login status upon init?
      cookie     : true, // set sessions cookies to allow your server to access the session?
      xfbml      : true  // parse XFBML tags on this page?
    });
    FB.getLoginStatus(function(response) {
      if (response.status === 'connected') {
        // connected
        //alert('connected');
      } else if (response.status === 'not_authorized') {
        // not_authorized
        login();
      } else {
        // not_logged_in
        login();
      }
    });
};
  (function(d){
     var js, id = 'facebook-jssdk', ref = d.getElementsByTagName('script')[0];
     if (d.getElementById(id)) {return;}
     js = d.createElement('script'); js.id = id; js.async = true;
     js.src = "//connect.facebook.net/en_US/all.js";
     ref.parentNode.insertBefore(js, ref);
   }(document));
   
function login() {
  alert('hi');
  FB.login(function(response) {
      if (response.authResponse) {
          // connected
          testAPI();
      } else {
          // cancelled
      }
  }, {scope:'read_stream,publish_stream,offline_access,read_friendlists,read_stream,read_mailbox,publish_actions,user_actions.music,user_actions.video,friends_actions.video,friends_status,user_status'});
}
  
function testAPI() {
  console.log('Welcome!  Fetching your information.... ');
  FB.api('/me', function(response) {
    console.log('Good to see you, ' + response.name + '.');
  });
}

function test() {
  FB.api('/me', function(response) {
  alert('Your name is ' + response.name);
});
}

function accessToken() {
    var x = document.getElementById('para');
    var keys = [];
    FB.getLoginStatus(function(response) {
    x.innerHTML=response.authResponse.accessToken;
  });
  }
function post() {
    var x = document.getElementById('para');
    var keys = [];
    FB.getLoginStatus(function(response) {
    x.innerHTML=response.authResponse.accessToken;
  });
  }
