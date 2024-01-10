$(document).ready(function() {
    $('#btn_translate').click(function() {
      let languageCode = $('#language_code').val();
      let apiUrl = 'https://www.fourtonfish.com/hellosalut/hello/';
  
      $.ajax({
        url: apiUrl + languageCode,
        type: 'GET',
        success: function(data) {
          $('#hello').text(data.hello);
        },
        error: function() {
          $('#hello').text('Error fetching translation.');
        }
      });
    });
  });
