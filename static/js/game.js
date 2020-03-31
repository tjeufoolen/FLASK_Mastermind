const colorOptionPins = document.querySelector(".color-options").querySelectorAll(".input-pin");
const gameInputs = document.querySelector(".game-input").querySelectorAll(".input-pin");
let draggedElement = null;

colorOptionPins.forEach(option => {
    option.addEventListener("dragstart", function() { draggedElement = this; });
    option.addEventListener("dragend", function() { draggedElement = null; });
});

gameInputs.forEach(input => {
    input.addEventListener("dragenter", function () {
        this.classList.add("hovered");
    });
    input.addEventListener("dragleave", function () {
        this.classList.remove("hovered");
    });
    input.addEventListener("drop", function (e) {
        e.preventDefault();
        this.classList.remove("hovered");

        const color = draggedElement.dataset.color;

        e.target.className = "";
        e.target.classList.add("input-pin", `bg-${color}`);
        e.target.querySelector("input[type='hidden']").value = color;

        validate();
    });
    input.addEventListener("dragover", function (e) {
        e.preventDefault();
    });
});

// validate();

function validate() {
    const submitBtn = document.querySelector("button[type='submit']");

    let canSubmit = true;
    gameInputs.forEach(pin => {
        const input = pin.querySelector("input[type='hidden']");
        if (input.value.length === 0) canSubmit = false;
    });

    if (canSubmit) {
        submitBtn.classList.remove("disabled");
        submitBtn.disabled = false;
    } else {
        submitBtn.classList.add("disabled");
        submitBtn.disabled = true;
    }
}