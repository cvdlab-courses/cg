

function EventEmitter () {
  this.handlers = {};
}

EventEmitter.prototype.on = function (event, handler) {
  var handlers_list = this.handlers[event];

  if (handlers_list === undefined) {
    handlers_list = this.handlers[event] = [];    
  }

  handlers_list.push(handler);
};

EventEmitter.prototype.emit = function (event) {
  var handlers_list = this.handlers[event];

  if (handlers_list === undefined) {
    return;
  }

  handlers_list.forEach(function (handler) {
    handler();
  });
};

// Shape inherits from EventEmitter
function Shape (x, y) {
  EventEmitter.call(this);
  this.x = x;
  this.y = y;
}

Shape.prototype = Object.create(EventEmitter.prototype);
Shape.prototype.constructor = Shape;

Shape.prototype.move = function (x, y) {
  this.x += x;
  this.y += y;
  this.emit('moved');
};

Shape.prototype.info = function () {
  console.log('x: ', this.x, ', y: ', this.y);
};

// Rectangle inherits from Shape
function Rectangle (x, y, width, height) {
  Shape.call(this, x, y); // call "super" constructor
  this.width = width;
  this.height = height;
}

Rectangle.prototype = Object.create(Shape.prototype);
Rectangle.prototype.constructor = Rectangle;

Rectangle.prototype.area = function () {
  return this.width * this.height;
};

Rectangle.prototype.info = function () {
  Shape.prototype.info.call(this);
  console.log('width: ', this.width, ', height: ', this.height);
};

Rectangle.prototype.position_info = function () {
  Shape.prototype.info.call(this);
};


// create new rectangle
var rect = new Rectangle(0, 0, 10, 20);

// position logger listen to 'moved' event
rect.on('moved', function () { 
  console.log('POSITION LOGGER: ')
  rect.position_info(); 
});

// verbose logger
rect.on('moved', function () { 
  console.log('VERBOSE LOGGER: ')
  console.log('area: ' + rect.area());
  rect.info(); 
});


