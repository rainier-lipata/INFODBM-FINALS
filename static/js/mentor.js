const user = JSON.parse(sessionStorage.getItem("user"));

if (!user) {

    window.location.href = "/login/";

}

document.getElementById("welcome").textContent =
    `Welcome back, ${user.FirstName} ${user.LastName}!`;

document.getElementById("role").textContent =
    `Role: ${user.Role}`;

async function loadPendingRequests() {

    const requests =
    await getPendingRequests(user.MentorID);

    console.log(requests);

    const container =
        document.getElementById("pending-requests");

    container.innerHTML = "";

    if (requests.length === 0) {

        container.innerHTML = `
            <div class="empty-state">
                No pending booking requests.
               </div>
        `;

        return;
    }

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

     if (sessions.length === 0) {

        container.innerHTML = `
            <div class="empty-state">
                No pending booking requests.
               </div>
        `;

        return;
    }


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

async function addAvailability(){

    const availability = {

        MentorID: user.MentorID,

        AvailableDate:
            document.getElementById("available-date").value,

        StartTime:
            document.getElementById("start-time").value,

        EndTime:
            document.getElementById("end-time").value

    };

    const result =
        await addAvailabilityRequest(availability);

    alert(result.Message);

    loadAvailability();

}

async function loadAvailability() {

    console.log("Loading availability...");

    const availability =
        await getAvailability(user.MentorID);

    const container =
        document.getElementById("mentor-availability");

    container.innerHTML = "";

     if (availability.length === 0) {

        container.innerHTML = `
            <div class="empty-state">
                No pending booking requests.
               </div>
        `;

        return;
    }

    availability.forEach(slot => {

        container.innerHTML += `

        <div class="session-card">

            <p>
                <strong>Date:</strong>
                ${slot.AvailableDate}
            </p>

            <p>
                <strong>Time:</strong>
                ${slot.StartTime}
                -
                ${slot.EndTime}
            </p>

            <button
                onclick="deleteAvailability(${slot.AvailabilityID})">

                Delete

            </button>

        </div>

        `;

    });

}

async function deleteAvailability(availabilityID){

    const result = await deleteAvailabilityRequest(availabilityID);

    alert(result.Message);

    loadAvailability();

}

function logout() {

    sessionStorage.clear();

    window.location.href = "/login/";

}


async function loadDashboard(){

    console.log("loadDashboard called");

    const dashboard = await getDashboard(user.MentorID);

    console.log(dashboard);

    document.getElementById("total-sessions").textContent =
        dashboard.TotalSessions;

    document.getElementById("scheduled-sessions").textContent =
        dashboard.ScheduledSessions;

    document.getElementById("completed-sessions").textContent =
        dashboard.CompletedSessions;
}

window.onload = function(){

    loadPendingRequests();

    loadMentorSessions();

    loadAvailability();

    loadDashboard()

};