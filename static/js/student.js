console.log("student.js loaded");

const user = JSON.parse(sessionStorage.getItem("user"));

if (!user) {

    window.location.href = "/login/";

}

document.getElementById("welcome").textContent =
    `Welcome back, ${user.FirstName} ${user.LastName}!`;

document.getElementById("role").textContent =
    `Role: ${user.Role}`;


function logout(){

    sessionStorage.clear();

    window.location.href="/login/";

}

async function searchMentors() {

    const topic = document.getElementById("topic").value;

    if (topic.trim() === "") {

        alert("Please enter a topic.");

        return;

    }

    const mentors = await searchMentorsRequest(topic);

    const results = document.getElementById("mentor-results");

    results.innerHTML = "";

    if (mentors.length === 0) {

        results.innerHTML ="<p>No mentors found.</p>";

        return;

    }

    mentors.forEach(mentor => {

        results.innerHTML += `
            <div class="mentor">
            
                <h4>${mentor.MentorName}</h4>

                <p><strong>Topic:</strong> ${mentor.TopicName}</p>

                <p><strong>Description:</strong> ${mentor.Description}</p>

                <p><strong>Skill Level:</strong> ${mentor.SkillLevel}</p>

                <p><strong>Experience:</strong> ${mentor.YearsExperience} years</p>

            <button onclick="bookMentor(${mentor.MentorID}, ${mentor.TopicID})">
                Book Session
            </button>
            
            <div
                id="booking-${mentor.MentorID}"
                class="booking-panel"
                style="display:none;">
                
            </div>
                
            </div>
        `;
    });

}

async function bookMentor(MentorID, TopicID) {

    const schedules = await getMentorAvailability(MentorID);
    console.log(schedules);

    const panel = document.getElementById(`booking-${MentorID}`);

    panel.style.display = "block";

    if (schedules.length === 0) {

        panel.innerHTML = "<p>No Available Schedules.</p>";

        return;
    }

    let options = "";

    schedules.forEach(schedule => {

        options += `
               <option value="${schedule.AvailabilityID}">
                   ${schedule.AvailableDate}
                   ${schedule.StartTime}
                   -
                   ${schedule.EndTime}
               </option>
           `;
    });

    panel.innerHTML = `
           <h4>Select Schedule</h4>
            
           <select id="availability-${MentorID}">
               ${options}
           </select>
            
           <textarea
               id="message-${MentorID}"
               placeholder="Enter your message"
               rows="4"></textarea>
                
           <button onclick="submitBooking(${MentorID}, ${TopicID})">
               Confirm Booking
           </button>
       `;

}

async function submitBooking(MentorID, TopicID) {

    const availabilityID =
        document.getElementById(`availability-${MentorID}`).value;

    const message =
        document.getElementById(`message-${MentorID}`).value;

    const booking = {

        StudentID: user.StudentID,
        MentorID: MentorID,
        AvailabilityID: availabilityID,
        TopicID: TopicID,
        Message: message

    };

    console.log(booking);

    try {

        const result = await createBookingRequest(booking);

        alert(result.Message);

    }
    catch(error){

    console.log(error);

    alert(error.Message || error.message || "Booking failed.");

}

}

async function loadStudentSessions() {

    const sessions = await getStudentSessions(user.StudentID);

    console.log(sessions);

    const container =
        document.getElementById("student-sessions");

    container.innerHTML = "";

     if (sessions.length === 0) {

        container.innerHTML = `
            <div class="empty-state">
                No pending booking requests.
               </div>
        `;

        return;
    }

    if (sessions.length === 0) {

        container.innerHTML =
            "<p>No sessions found.</p>";

        return;
    }

    sessions.forEach(session => {

        container.innerHTML += `

            <div class="session-card">

                <h4>
                    Mentor: ${session.MentorName}
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

            </div>

        `;

    });

}

window.onload = function(){

    document.getElementById("welcome").textContent =
        `Welcome back, ${user.FirstName} ${user.LastName}!`;

    document.getElementById("role").textContent =
        `Role: ${user.Role}`;

    loadStudentSessions();

};