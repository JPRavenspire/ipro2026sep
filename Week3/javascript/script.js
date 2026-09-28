// DARK MODE Javascript Code

const darkButton = document.querySelector("#dark-toggle");

darkButton.addEventListener("click", () => {

    document.body.classList.toggle("dark-mode");
});



















// FORM Javascript Code

console.log("Hello World!")

const button = document.querySelectorAll("button");
const form = document.querySelector("#appointment");
const nameInput = document.querySelector("#name");

// button.forEach(webButton => {
//     webButton.addEventListener("click", () => {
//         alert("Reservation Complete!");
//     });
// });

form.addEventListener("submit", (event) => {
    event.preventDefault();

    // const name = nameInput.value.trim();
    const name = nameInput.value;
    console.log(name);

    if (name === "") {
        alert("Name is required.")
        return;
    }
})