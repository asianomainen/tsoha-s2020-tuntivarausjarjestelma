$(document).ready(function() {
    $(function() {
        $('.trigger').change(function() {
          $(this).next('.showthis').toggle(this.checked);
        })
      });
});

// const signUpButton = document.getElementById('signUp');
// const signInButton = document.getElementById('signIn');
// const container = document.getElementById('container');

// signUpButton.addEventListener('click', () => {
// 	container.classList.add("right-panel-active");
// });

// signInButton.addEventListener('click', () => {
// 	container.classList.remove("right-panel-active");
// });