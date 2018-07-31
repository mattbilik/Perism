

var user_id = 0;
let auth_token = 0;

$("#button").onclick = function loadAuth(user_id, auth_token){
console.log('Authenticated')
document.getElementById('headline').innerHTML = "Checking..."
apiLoad();
}

function apiLoad(){
  let xhr  =  new XMLHttpRequest();
xhr.send('GET','put the fucking link in here','FALSE');
}
