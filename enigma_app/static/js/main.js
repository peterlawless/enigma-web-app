var alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
                'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
                'Y', 'Z'];

var slow_index = 0;
var middle_index = 0;
var fast_index = 0;

$('.fast-letter').html(alphabet[fast_index]);
$('.middle-letter').html(alphabet[middle_index]);
$('.slow-letter').html(alphabet[slow_index]);



$('.up').click(function () {
  if ($(this).parent().parent().hasClass('slow-rotor')) {
    slow_index = (slow_index + 1) % 26;
    $('.slow-letter').html(alphabet[slow_index]);
  } else if ($(this).parent().parent().hasClass('middle-rotor')) {
    middle_index = (middle_index + 1) % 26;
    $('.middle-letter').html(alphabet[middle_index]);
  } else if ($(this).parent().parent().hasClass('fast-rotor')) {
    fast_index = (fast_index + 1) % 26;
    $('.fast-letter').html(alphabet[fast_index]);
  }
});

$('.down').click(function () {
  if ($(this).parent().parent().hasClass('slow-rotor')) {
    if (slow_index === 0) {slow_index = slow_index + 26;}
    slow_index = (slow_index - 1) % 26;
    $('.slow-letter').html(alphabet[slow_index]);
  } else if ($(this).parent().parent().hasClass('middle-rotor')) {
    if (middle_index === 0) {middle_index = middle_index + 26;}
    middle_index = (middle_index - 1) % 26;
    $('.middle-letter').html(alphabet[middle_index]);
  } else if ($(this).parent().parent().hasClass('fast-rotor')) {
    if (fast_index === 0) {fast_index = fast_index + 26;}
    fast_index = (fast_index - 1) % 26;
    $('.fast-letter').html(alphabet[fast_index]);
  }
});

$('button').click(function(event) {
  event.preventDefault();
  var rotors = [];
  var settings = [];
  $('select').each(function(i, e) {
    rotors.push(e.value);
  });
  settings.push($('.slow-letter').html());
  settings.push($('.middle-letter').html());
  settings.push($('.fast-letter').html());
  console.log(rotors);
  console.log(settings);
  if (rotors.length === 3 && settings.length === 3) {
    $.ajax({type:"GET",
            url: '/encrypt/',
            data: {'rotor': rotors, 'setting': settings, 'letter': 'A'},
            traditional: true}
          ).done(function(response) {console.log(response);}); // end .done()
  };
});
