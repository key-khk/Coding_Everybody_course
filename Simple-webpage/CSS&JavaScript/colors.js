function setLinksColor(color){
  var alist = document.querySelectorAll('a');
  var i = 0;
  while(i < alist.length){
    alist[i].style.color = color;
    i = i + 1;
  }
}
function BodysetColor(color){
  document.querySelector('body').style.color = color;
}
function BodysetBackgroundColor(color){
  document.querySelector('body').style.backgroundColor = color;
}
  function offonHandler(self){
    var target = document.querySelector('body')
      if (self.value === 'OFF'){
        BodysetBackgroundColor('black');
        BodysetColor('white');
        self.value = 'ON';
        setLinksColor('powderblue');

      } else {
        BodysetBackgroundColor('white');
        BodysetColor('black');
        self.value = 'OFF';
        setLinksColor('blue');
      }
  }
