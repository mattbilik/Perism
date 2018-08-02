window.addEventListener('load', function() {


  var loginBtn = document.getElementById('btn-login');
  loginBtn.addEventListener('click', function(e) {
    var auth = document.getElementById('password').innerHTML
    if(auth == '12345'){

      window.location.href = "http://www.perism.net/survey";

    }
    else{
      document.getElementById('error-message').style.display = "inline";
    }
  });

});
