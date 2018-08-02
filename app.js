window.addEventListener('load', function() {

  var webAuth = new auth0.WebAuth({
    domain: 'perism.auth0.com',
    clientID: 'zAMeDEMvV92aLChquVVnPCh2f7otpytC',
    responseType: 'token id_token',
    audience: 'https://perism.auth0.com/userinfo',
    scope: 'openid',
    redirectUri: window.location.href
  });

  var loginBtn = document.getElementById('btn-login');

  loginBtn.addEventListener('click', function(e) {
    e.preventDefault();
    webAuth.authorize();
  });

});
