const API_URL = "http://127.0.0.1:8000/api";

async function loginRequest(email, password) {

    const response = await fetch(`${API_URL}/accounts/login/`, {

        method: "POST",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify({
            Email: email,
            PasswordHash: password
        })

    });

    return await response.json();

}

async function searchMentorsRequest(topic) {

    const response = await fetch(
        `${API_URL}/students/search-mentors/?topic=${encodeURIComponent(topic)}`
    );

    return await response.json();


}

async function getMentorAvailability(mentorID) {

    const response = await fetch(
        `${API_URL}/mentors/availability/${mentorID}/`
    );

    return await response.json();
}

async function createBookingRequest(data) {

    const response = await fetch(`${API_URL}/booking/create/`, {

        method:"POST",

        headers: {
            "Content-Type":"application/json"

        },

        body: JSON.stringify(data)
    });

    const result = await response.json();

    if (!response.ok) {
        throw result;
    }

    return result;
}


async function getPendingRequests(mentorID) {

    const response = await fetch(
        `/api/booking/pending/${mentorID}/`
    );

    return await response.json();

}

async function approveBooking(requestID) {

    const response = await fetch (
        `${API_URL}/booking/approve/${requestID}/`,
        {
            method: "PUT"
        }
    );

    return await response.json();
}