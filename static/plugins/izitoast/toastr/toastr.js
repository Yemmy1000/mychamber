
"use strict";

function tryc(a, b, c, d){
  if (a  === undefined){
  a = '';
}
if (b  === undefined){
  b = '';
}
if (c  === undefined){
  c = '';
}
// if (d  === undefined){
//   d = '';
// }
  try{
                showToast(a, b, c, d);
            }
            catch(err){
                // alert(err);
            }

}
function showToast(type, title, message, position) {


if (title  === undefined){
  title = '';
}


if (type  === undefined){
  type = '';
}
if (message  === undefined){
  message = '';
}


if (position  === undefined){
  position = 'topCenter';
}

if (type === 'success'){

  iziToast.success({
    title: title,
    message: message,
    position: position
  });

}
else if (type === 'info'){

  iziToast.info({
    title: title,
    message: message,
    position: position
  });

}
else if (type === 'warning'){

  iziToast.warning({
    title: title,
    message: message,
    position: position
  });

}
else if (type === 'error'){

  iziToast.error({
    title: title,
    message: message,
    position: position
  });

}
else{

}
}

// }
