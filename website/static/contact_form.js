const inputs = document.querySelectorAll(".input");

function focusFunc() {
  let parent = this.parentNode;
  parent.classList.add("focus");
}

function blurFunc() {
  let parent = this.parentNode;
  if (this.value == "") {
    parent.classList.remove("focus");
  }
}

inputs.forEach((input) => {
  input.addEventListener("focus", focusFunc);
  input.addEventListener("blur", blurFunc);
});

SubmitEvent.addEventListener('submit', (e)=>{

    e.preventDefault();
    console.log("Clicked");

    //send email
    Email.send({
        SecureToken : " 2c2670bc-bed8-4994-bd34-ef4e1d4d6bbb",
        To : 'embersonlatogm@cardiff.ac.uk',
        From : 'MiGiu202017@gmail.com',
        Subject : "Thanks for contacting Giuly's Studio",
        Body : "We will reply to your message shortly"
    }).then(
    message => alert(message)
    );

});

