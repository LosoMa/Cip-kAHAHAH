const popupButton = document.querySelector("");
const popupWindow = document.querySelector("");

popupButton.addEventListener("click", function() {
    popupWindow.style.display = "block";
});

const closeButton = document.querySelector("#close-button");
closeButton.addEventListener("click", () => {
    popupWindow.style.display = "none";
})