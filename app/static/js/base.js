const modalRegister = document.getElementById('id01');
const modalLogin = document.getElementById('id02');

window.addEventListener("click", function(event) {
    if (event.target === modalRegister) {
      modalRegister.style.display = "none";
    }else if(event.target === modalLogin){
      modalLogin.style.display = "none";
    }
});