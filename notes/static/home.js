

$(function(){
  let hash = window.location.hash
  if(hash === "#useradded") {
    $('#col-js').prepend('<h2 class="text-success fw-bold text-decoration-underline mb-2">You successfully added a user</h2>')
  }
  else if(hash === "#signedin") {
    $('#col-js').prepend('<h2 class="text-success fw-bold text-decoration-underline mb-2">You signed in!</h2>')
  }
  else if(hash === "#notsignedin") {
    $('#col-js').prepend('<h2 class="text-danger fw-bold text-decoration-underline mb-2">Incorrect username or password, try again!</h2>')
  }
});