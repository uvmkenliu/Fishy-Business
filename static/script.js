//define variables
var upButton = $('.upButton');
var rightButton = $('.rightButton');
var downButton = $('.downButton');
var leftButton = $('.leftButton');
var stringUp = $('.upStringButton');
var stringDown = $('.downStringButton');

upButton.on("mousedown",up);
downButton.on("mousedown",down);
rightButton.on("mousedown",right);
leftButton.on("mousedown",left);
stringUp.on("mousedown",strUp);
stringDown.on("mousedown",strDown);

upButton.on("mouseup",stopMotor);
downButton.on("mouseup",stopMotor);
rightButton.on("mouseup",stopMotor);
leftButton.on("mouseup",stopMotor);
stringUp.on("mouseup",stopMotor);
stringDown.on("mouseup",stopMotor);

//Check what key is pressed
document.onkeydown = function(e){
    switch (e.keyCode) {
        case 37:
            left();
            break;
        case 38:
            up();;
            break;
        case 39:
            right();
            break;
        case 40:
            down();;
            break;
        case 87:
            strUp();;
            break;
        case 83:
            strDown();;
            break;
    };
};
//Direction Funtions
function up(){
    $.ajax({
        url: "/vertical_up",
        type: "post",
        success: function(response) {
            console.log(response);
        }
    });
};
function down(){
    $.ajax({
        url: "/vertical_down",
        type: "post",
        success: function(response) {
            console.log(response);
        }
    });
};
function right(){
    $.ajax({
        url: "/horizontal_right",
        type: "post",
        success: function(response) {
            console.log(response);
        }
    });
};
function left(){
    $.ajax({
        url: "/horizontal_left",
        type: "post",
        success: function(response) {
            console.log(response);
        }
    });
};
function strUp(){
    $.ajax({
        url: "/string_up",
        type: "post",
        success: function(response) {
            console.log(response);
        }
    });
};
function strDown(){
    $.ajax({
        url: "/string_down",
        type: "post",
        success: function(response) {
            console.log(response);
        }
    });
};
function stopMotor(){
    $.ajax({
        url: "/stop_motor",
        type: "post",
        success: function(response) {
            console.log(response);
        }
    });
};

//===================Leaderboard stuff======================



//===================Timer Stuff============================
$('.startTimer').on('click', startTimer);

$('.oneMinute').on('click', function(){
    $('.timer').html("<span class = 'minutes'>0</span>:<span class = 'seconds'>12</span>");
    $('.timer').css('color', 'white');
})
$('.twoMinute').on('click', function(){
    $('.timer').html("<span class = 'minutes'>2</span>:<span class = 'seconds'>00</span>");;
    $('.timer').css('color', 'white');
})
$('.threeMinute').on('click', function(){
    $('.timer').html("<span class = 'minutes'>3</span>:<span class = 'seconds'>00</span>");
    $('.timer').css('color', 'white');
})

function startTimer(){
    //hide time change buttons
    $('.oneMinute').css('display', 'none');
    $('.twoMinute').css('display', 'none');
    $('.threeMinute').css('display', 'none');

    //get minute and second html values
    var minutes = $('.minutes').html();
    var seconds = $('.seconds').html();
    console.log("seconds "+seconds);
    console.log("minutes "+minutes);

    var fraction = 100/((minutes * 60)+(seconds * 1));

    //start countdown
    var countdown = setInterval(function() {

        if((minutes != 0 || seconds != 0) && seconds <= 60){
            if(seconds == 00 && minutes >0){
                minutes--;
                $('.seconds').html("60");
                seconds = $('.seconds').html();
            }
            //subtract a second
            seconds--;
            if(seconds <= 9){
                $('.minutes').html(minutes);
                $('.seconds').html("0"+seconds);
            }else{
                $('.minutes').html(minutes);
                $('.seconds').html(seconds);
            }
            if(seconds <= 10 && minutes == 0){
                $('.timer').css('color', 'orange');
            }
            if(seconds <= 5 && minutes == 0){
                $('.timer').css('color', 'red');
            }
        }
        else if (seconds <= 0 && minutes == 0){
            clearInterval(countdown);

            $('.oneMinute').css('display', 'block');
            $('.twoMinute').css('display', 'block');
            $('.threeMinute').css('display', 'block');
        }
        //get total seconds
        var secondsLeft = (minutes * 60) + (seconds * 1);
        //how high up the background color is
        //when it gets to top time is up
        var colorHeight = 100 - (fraction * secondsLeft);
        $('.timerColor').css('height', colorHeight + '%');

    }, 1000);
};
