/*
// Get DOM Elements
const modal = document.querySelector('.my-modal');
const modalBtn = document.querySelector('.modal-btn');
const closeBtn = document.querySelector('.close');



// Events
modalBtn.addEventListener('click', openModal);
closeBtn.addEventListener('click', closeModal);
window.addEventListener('click', outsideClick);

// Open
function openModal() {
  modal.style.display = 'block';
}

// Close
function closeModal() {
  modal.style.display = 'none';
}

// Close If Outside Click
function outsideClick(e) {
  if (e.target == modal) {
    modal.style.display = 'none';
  }
}
*/





 /*back to top button*/
 const toTop = document.querySelector(".to-top");

window.addEventListener("scroll", () => {
  if (window.pageYOffset > 800) {
    toTop.classList.add("active");
  } else {
    toTop.classList.remove("active");
  }
})




