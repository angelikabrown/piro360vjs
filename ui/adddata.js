const API_URL = `http://localhost:8080`;


function doPostOfForm(event) {
    event.preventDefault();
    const formData = new FormData(document.getElementById('dataform'));
    const object = {};
    formData.forEach((value, key) => {
        object[key] = value;
    });
    object['timestamp'] = Date.now().toString();

    const json = JSON.stringify(object);

    fetch(`${API_URL}/data`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: json,
    })
        .then(response => response.json())
        .then(data => {
            console.log('Success:', data);
            window.location.href = `/ui/datadetail.html?dataid=${data.id}`;
        })
        .catch(error => console.error('Error:', error));
}

// async function postJSON(data) {
//     try {
//         const response = await fetch(`${API_URL}/data`, {
//             method: 'POST', // or 'PUT'
//             headers: {
//                 accept: '*/*',
//                 'Content-Type': 'application/json',
//             },
//             body: data, // This was ALSO Stringifying the data
//             // body: JSON.stringify(data)
//             // but this is already a string because I did the stringify above
//         });

//         const result = await response.json();
//         console.log('Success:', result);

//     } catch (error) {
//         console.error('Error:', error);
//     }
// }
window.addEventListener(
    'DOMContentLoaded',
    function () {
        const form = document.getElementById('dataform');
        const button1 = document.getElementById('button1');
        console.log('form is ', form, 'button1 is ', button1, 'doPostOfForm is ', doPostOfForm);

        form.addEventListener('submit', doPostOfForm);
    },
    false,
);