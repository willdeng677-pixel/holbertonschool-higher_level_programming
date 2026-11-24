#!/usr/bin/node

document.addEventListener('DOMContentLoaded', function () {
  const myList = document.querySelector('#my_list');

  document.querySelector('#add_item').addEventListener('click', function () {
    const newItem = document.createElement('li');
    newItem.textContent = 'Item';
    myList.appendChild(newItem);
  });

  document.querySelector('#remove_item').addEventListener('click', function () {
    if (myList.lastElementChild) {
      myList.removeChild(myList.lastElementChild);
    }
  });

  document.querySelector('#clear_list').addEventListener('click', function () {
    myList.innerHTML = '';
  });
});
