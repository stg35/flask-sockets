$('#sign_form').on('submit', function() {
  //var socket = io.connect('http://127.0.0.1:5000');
  var username = $('#username_field').val();
  console.log(username);
  //socket.emit('username', username);
  alert('Hello, ' + username);
});
