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
    var auth = document.getElementById('password').innerHTML
    if(auth === '12345'){

      window.location.href = "http://www.perism.net/survey";

    }
    else{
      document.getElementById('error-message').style.display = "inline";
    }
  });

});
