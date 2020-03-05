$('#sign_form').on('submit', function() {
  var username = $('#username_field').val();
  console.log(username);
  alert('Hello, ' + username);
});
