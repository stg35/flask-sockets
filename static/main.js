function formhelper() {

  if (document.getElementById('person-name')) {
    var personname = document.getElementById('person-name').value;
    name = personname;
    var toremove = document.getElementById('person-name');
    toremove.remove();
  }

  text1 = '<div class="chat-body white p-3 ml-2 z-depth-1"><div class="header"><strong>'+name+'</strong></div><p class="mb-0">';
  text2 = '</p></div>';

  console.log(name);

  var val = document.getElementById('exampleFormControlTextarea2').value;
  var parent = document.getElementById('list');
  var li = document.createElement('li');
  li.className = 'd-flex justify-content-between mb-4 bubble';
  li.innerHTML = text1 + val + text2;
  console.log(parent);
  console.log(li);
  parent.append(li);
  document.getElementById('exampleFormControlTextarea2').value = "";
}
