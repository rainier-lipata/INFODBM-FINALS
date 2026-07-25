async function login() {

    const email = document.getElementById("email").value;

    const password = document.getElementById("password").value;

    const response = await fetch(

        `${BASE_URL}/accounts/login/`,

        {

            method:"POST",

            headers:{

                "Content-Type":"application/json"

            },

            body:JSON.stringify({

                Email:email,

                PasswordHash:password

            })

        }

    );

    const data = await response.json();

    if(response.ok){

        sessionStorage.setItem(

            "UserID",

            data.user.UserID

        );

        sessionStorage.setItem(

            "Role",

            data.user.Role

        );

        sessionStorage.setItem(

            "FirstName",

            data.user.FirstName

        );

        if(data.user.Role==="Student"){

            window.location.href="student-dashboard.html";

        }

        else{

            window.location.href="mentor-dashboard.html";

        }

    }

    else{

        alert(data.message);

    }

}