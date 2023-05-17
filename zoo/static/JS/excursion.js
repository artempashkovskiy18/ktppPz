document.addEventListener("DOMContentLoaded", function () {
    $("#form").one('submit', function (event) {
        event.preventDefault();
        let inputs = document.getElementsByClassName("inputBox");
        let isValid = true;

        for (let i = 0; i < inputs.length; i++) {
            if (inputs[i].value === "") {
                inputs[i].style.border = "2px solid red";
                isValid = false
            } else {
                inputs[i].style.border = "1px solid black";
            }

            if (inputs[i].id === "phone") {
                let regularExpression = new RegExp("[+]?38[0-9]{10}");

                if (!regularExpression.test(inputs[i].value)) {
                    inputs[i].style.border = "2px solid red";
                    isValid = false;
                } else {
                    inputs[i].style.border = "1px solid black";
                }
            }
        }

        if (isValid) {
            $(this).submit;
        }
    })
});
