async function login() {

    const email = document.getElementById("email").value;

    const password = document.getElementById("password").value;

    if (email === "" || password === "") {

        alert("Please enter your email and password.");

        return;
    }

    try {

        const result = await loginRequest(email, password);
        console.log(result);

        sessionStorage.setItem(
            "user",
            JSON.stringify(result.user)
        );

        if (result.user.Role === "Student") {

            window.location.href = "/student-dashboard/";

        } else if (result.user.Role === "Mentor") {

            window.location.href = "/mentor-dashboard/";

        }


    }

    catch(error) {

        console.error(error);

        alert("Login failed.");
    }
}
