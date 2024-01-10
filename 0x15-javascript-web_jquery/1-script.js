document.addEventListener('DOMContentLoaded', function () {
    document.querySelector('header').style.color = '#FF0000';
    document.querySelector('DIV#red_header').addEventListener('click', function () {
      document.querySelector('header').style.color = '#FF0000';
    });
    document.querySelector('DIV#green_header').addEventListener('click', function () {
      document.querySelector('header').style.color = '#00FF00';
    });
    document.querySelector('DIV#blue_header').addEventListener('click', function () {
      document.querySelector('header').style.color = '#0000FF';
    });
  });
