var alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
                'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
                'Y', 'Z'];

var slow_index = 0;
var middle_index = 0;
var fast_index = 0;

$('.window').html('<span>' + alphabet[0] + '</span>');

$('.up').click(function () {
  if ($(this).parent().parent().hasClass('slow-rotor')) {
    slow_index = (slow_index + 1) % 26;
    $(this).parent().prev().html('<span>' + alphabet[slow_index] + '</span>');
  } else if ($(this).parent().parent().hasClass('middle-rotor')) {
    middle_index = (middle_index + 1) % 26;
    $(this).parent().prev().html('<span>' + alphabet[middle_index] + '</span>');
  } else if ($(this).parent().parent().hasClass('fast-rotor')) {
    fast_index = (fast_index + 1) % 26;
    $(this).parent().prev().html('<span>' + alphabet[fast_index] + '</span>');
  }
});

$('.down').click(function () {
  if ($(this).parent().parent().hasClass('slow-rotor')) {
    if (slow_index === 0) {slow_index = slow_index + 26;}
    slow_index = (slow_index - 1) % 26;
    $(this).parent().prev().html('<span>' + alphabet[slow_index] + '</span>');
  } else if ($(this).parent().parent().hasClass('middle-rotor')) {
    if (middle_index === 0) {middle_index = middle_index + 26;}
    middle_index = (middle_index - 1) % 26;
    $(this).parent().prev().html('<span>' + alphabet[middle_index] + '</span>');
  } else if ($(this).parent().parent().hasClass('fast-rotor')) {
    if (fast_index === 0) {fast_index = fast_index + 26;}
    fast_index = (fast_index - 1) % 26;
    $(this).parent().prev().html('<span>' + alphabet[fast_index] + '</span>');
  }
});
