// script that updates the text of the <header>
// element to New Header!!! when the user clicks
// on DIV#update_header

$(document).ready(function () {
  $('#update_header').click(function () {
    $('header').text('New Header!!!');
  });
});
