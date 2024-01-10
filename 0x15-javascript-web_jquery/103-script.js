const $ = window.$;

$(document).ready(function() {
  $('#btn_translate').click(function() {
    translateHello();
  });

  $('#language_code').keypress(function(event) {
    if (event.which === 13) {
      translateHello();
    }
  });

  function translateHello() {
    const languageCode = $('#language_code').val();
    const apiUrl = `https://www.fourtonfish.com/hellosalut/hello/${languageCode}`;

    $.get(apiUrl, function(data) {
      $('#hello').text(data.hello);
    });
  }
});
