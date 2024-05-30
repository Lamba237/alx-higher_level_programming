// script that toggles the class of the <header>
// script that toggles the class of the <header>
$(document).ready(function () {
  $('#toggle_header').click(function () {
    if ($('header').hasClass('red')) {
      $('header').removeClass('red').addClass('green');
    } else if ($('header').hasClass('green')) {
      $('header').removeClass('green').addClass('red');
    }
  });
});
