function checkPassword() {

    let password =
    document.getElementById("passwordInput").value;

    let result =
    document.getElementById("result");

    if (password.length < 6) {

        result.innerHTML =
        "Weak Password";

        result.style.color = "red";

    }

    else if (password.length < 10) {

        result.innerHTML =
        "Medium Password";

        result.style.color = "orange";

    }

    else {

        result.innerHTML =
        "Strong Password";

        result.style.color = "lime";

    }
}