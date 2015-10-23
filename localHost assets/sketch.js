

// Keep track of our socket connection
var socket;

function setup() {
  createCanvas(windowWidth, windowHeight);
  //background(0);
  // Start a socket connection to the server
  // Some day we would run this server somewhere else
  socket = io.connect('http://10.1.1.103:8080');
  // We make a named event called 'mouse' and write an
  // anonymous callback function
  socket.on('mouse',
    // When we receive data
    function(data) {
      console.log("Got: " + data.x + " " + data.y);
      // Draw a blue circle
      fill(0,0,255);
      noStroke();
      ellipse(data.x,data.y,80,80);
    }
  );
}

function draw() {
  // Nothing
}

function touchMoved() {
  // Draw some white circles
  fill(0);
  noStroke();
  ellipse(touchX,touchY,80,80);
  // Send the mouse coordinates
  sendmouse(touchX,touchY);
}

// Function for sending to the socket
function sendmouse(xpos, ypos) {
  // We are sending!
 // console.log("sendmouse: " + xpos + " " + ypos);
  
  // Make a little object with  and y
  var data = {
    x: xpos,
    y: ypos
  };

  // Send that object to the socket
  socket.emit('mouse',data);
}