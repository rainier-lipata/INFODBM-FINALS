const user = JSON.parse(sessionStorage.getItem("user"));

if (!user) {

    window.location.href = "/login/";

}

async function loadPendingRequests() {

    const requests =
    await getPendingRequests(user.MentorID);

    console.log(requests);

    const container =
        document.getElementById("pending-requests");

    container.innerHTML = "";

    requests.forEach(request => {

        container.innerHTML += `
        <div class="request-card">

            <h4>${request.StudentName}</h4>

            <p>
                Topic:
                ${request.TopicName}
            </p>

            <p>
                ${request.Message}
            </p>

            <button
                onclick="approve(${request.RequestID})">

                Approve
            </button>

        </div>
        `;
    });

}

async function approve(requestID) {

    const response = await fetch(
        `/api/booking/approve/${requestID}/`,
        {
            method: "PUT",
            headers:{
                "Content-Type":"application/json"
            }
        }
    );


    const data = await response.json();


    console.log(data);


    if(response.ok){

        alert(data.Message);

        loadPendingRequests();

    }
    else{

        alert(data.message);

    }

}

async function loadMentorSessions(){

    const response = await fetch(
    `/api/booking/sessions/mentor/${user.MentorID}/`
    );


    const sessions = await response.json();


    console.log(sessions);


    const container =
        document.getElementById("mentor-sessions");


    container.innerHTML = "";


    sessions.forEach(session => {


        let actionButton = "";


        if(session.Status !== "completed"){

            actionButton = `

                <button onclick="completeSession(${session.SessionID})">

                    Mark Completed

                </button>

            `;

        }
        else{

            actionButton = `

                <p>
                    Session Completed
                </p>

            `;

        }


        container.innerHTML += `

        <div class="session-card">

            <h4>
                Student: ${session.StudentName}
            </h4>


            <p>
                Date:
                ${session.SessionDate}
            </p>


            <p>
                Time:
                ${session.StartTime}
                -
                ${session.EndTime}
            </p>


            <p>
                Status:
                ${session.Status}
            </p>


            ${actionButton}


        </div>

        `;

    });

}

async function completeSession(sessionID){

    const response = await fetch(
        `/api/booking/sessions/complete/${sessionID}/`,
        {
            method:"PUT"
        }
    );


    const data = await response.json();


    alert(data.Message);


    loadMentorSessions();

}

function logout() {

    sessionStorage.clear();

    window.location.href = "/login/";

}

window.onload = function(){

    loadPendingRequests();

    loadMentorSessions();

};