const API_URL = `http://localhost:8080`;


function doPostOfForm(event) {
    event.preventDefault();
    var floozy = new FormData(document.getElementById('dataform'));
    
    var object = {};
    for (var p of floozy) {
        let name = p[0];
        let value = p[1];
        object[name] = value;
    }
    object['timestamp'] = Date.now().toString();
    console.log('object is ', object);
    var json = JSON.stringify(object);
    // only need to stringify once
    postJSON(json);
    }

async function postJSON(data) {
    try {
        const response = await fetch(`${API_URL}/data`, {
            method: 'POST', // or 'PUT'
            headers: {
                accept: '*/*',
                'Content-Type': 'application/json',
            },
            body: data, // This was ALSO Stringifying the data
            // body: JSON.stringify(data)
            // but this is already a string because I did the stringify above
        });

        const result = await response.json();
        console.log('Success:', result);

        // // Add the new data to the page
        // const DataListDiv = document.getElementById('data-list');
        // const newDiv = document.createElement('div');
        // newDiv.innerHTML = `
        //     <h3>${result.cycle_day}</h3>
        //     <p>Temperature: ${result.temperature}</p>
        //     <p>Mood: ${result.mood}</p>
        //     <p>Energy: ${result.energy}</p>
        //     <p>Notes: ${result.notes}</p>
        //     <p>Date: ${result.date}</p>
        // `;
        // DataListDiv.appendChild(newDiv);

    } catch (error) {
        console.error('Error:', error);
    }
}
window.addEventListener(
    'DOMContentLoaded',
    function () {
        const form = document.getElementById('dataform');
        const button1 = document.getElementById('button1');
        console.log('form is ', form, 'button1 is ', button1, 'doPostOfForm is ', doPostOfForm);

        form.addEventListener(button1, doPostOfForm);
    },
    false,
);