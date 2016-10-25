var alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
                'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
                'Y', 'Z'];

$('.fast-letter').html('A');
$('.middle-letter').html('A');
$('.slow-letter').html('A');

var cipher_letter;
var fast_rotor_turnover;
var middle_rotor_turnover;
var letter;

function rotate(domElement, direction) {
  if (direction === "forward") {
    increment = 1;
  } else if (direction === "backward") {
    increment = -1;
  }
  domElement.html(alphabet[(alphabet.indexOf(domElement.html()) + 26 + increment) % 26]);
}

function validate_selection() {

}

$('.up').click(function () {
  if ($(this).parent().parent().hasClass('slow-rotor')) {
    rotate($('.slow-letter'), "forward");
  } else if ($(this).parent().parent().hasClass('middle-rotor')) {
    rotate($('.middle-letter'), "forward");
  } else if ($(this).parent().parent().hasClass('fast-rotor')) {
    rotate($('.fast-letter'), "forward");
  }
});

$('.down').click(function () {
  if ($(this).parent().parent().hasClass('slow-rotor')) {
    rotate($('.slow-letter'), "backward");
  } else if ($(this).parent().parent().hasClass('middle-rotor')) {
    rotate($('.middle-letter'), "backward");
  } else if ($(this).parent().parent().hasClass('fast-rotor')) {
    rotate($('.fast-letter'), "backward");
  }
});

var timesCalled = 0;

$(document).keydown(function(event) {
  letter = String.fromCharCode(event.keyCode);
  if (alphabet.includes(letter)) {
    if (timesCalled < 2) {
      timesCalled++;
    };
    if (timesCalled === 1) {
      var rotors = [];
      var settings = [];
      $('select').each(function(i, e) {
        rotors.push(e.value);
      });
      settings.push($('.slow-letter').html());
      settings.push($('.middle-letter').html());
      settings.push($('.fast-letter').html());
      if (rotors.length === 3 && settings.length === 3) {
        $.ajax({type:"GET",
                url: '/encrypt/',
                data: {'rotor': rotors, 'setting': settings},
                traditional: true}
              ).done(function(response) {
                if (response.fast_rotor_turnover && response.middle_rotor_turnover) {
                  rotate($('.slow-letter'), "forward");
                  rotate($('.middle-letter'), "forward");
                  rotate($('.fast-letter'), "forward");
                } else if (response.fast_rotor_turnover) {
                  rotate($('.middle-letter'), "forward");
                  rotate($('.fast-letter'), "forward");
                } else {
                  rotate($('.fast-letter'), "forward");
                }
              }); // end .done()
      }; // end if (rotors.length === 3 && settings.length === 3)
      rotors = [];
      settings = [];
      $('select').each(function(i, e) {
        rotors.push(e.value);
      });
      settings.push($('.slow-letter').html());
      settings.push($('.middle-letter').html());
      settings.push($('.fast-letter').html());
      if (rotors.length === 3 && settings.length === 3) {
        $.ajax({type:"GET",
                url: '/encrypt/',
                data: {'rotor': rotors, 'setting': settings, 'letter':letter},
                traditional: true}
              ).done(function(response) {
                $('#' + response.cipher_letter).addClass('glow');
              }); // end .done()
      }; // end if (rotors.length === 3 && settings.length === 3)
    }; // end if (timesCalled === 1)
  }; // end if (alphabet.includes(letter))
}).keyup(function() {
  $('.glow').removeClass('glow');
  timesCalled = 0;
});
