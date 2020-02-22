

// function sock() {
//         var socket = io.connect('http://0.0.0.0:5000');
//
//         $('#send_button').on('click', function(){
//             socket.emit('message', $('#exampleFormControlTextarea2').val());
//             if (document.getElementById('person-name')) {
//                 var personname = document.getElementById('person-name').value;
//                 var name1 = personname;
//                 var toremove = document.getElementById('person-name');
//                 toremove.remove();
//             }
//             name = name1;
//             console.log(name);
//             socket.emit('message', name);
//         });
//
//         socket.on('message_sent', function(msg){
//             $('#list').append(text3+text1+name+text12+msg+text2+'</li>');
//             console.log(msg);
//         });
//         console.log('connected');
// }

// function formhelper() {
//
//
//
//
//     if (document.getElementById('person-name')) {
//       var personname = document.getElementById('person-name').value;
//       var name = personname;
//       var toremove = document.getElementById('person-name');
//       toremove.remove();
//     }
//
//     text1 = '<div class="chat-body white p-3 ml-2 z-depth-1"><div class="header"><strong>' + name + '</strong></div><p class="mb-0">';
//     text2 = '</p></div>';
//
//     console.log(name);
//
//     //var val = document.getElementById('exampleFormControlTextarea2').value;
//     var val = msg;
//     var parent = document.getElementById('list');
//     var li = document.createElement('li');
//     li.className = 'd-flex justify-content-between mb-4 bubble';
//     li.innerHTML = text1 + val + text2;
//     console.log(parent);
//     console.log(li);
//     parent.append(li);
//     document.getElementById('exampleFormControlTextarea2').value = "";
//   });
// }
//
