#!/usr/bin/node

document.addEventListener('DOMContentLoaded', function () {
  document.querySelector('#btn_translate').addEventListener('click', function () {
    const langCode = document.querySelector('#language_code').value;
    fetch(`https://stefanbohacek.com{langCode}`)
      .then(function (response) {
        return response.json();
      })
      .then(function (data) {
        document.querySelector('#hello').textContent = data.hello;
      });
  });
});
