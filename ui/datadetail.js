const API_URL = `http://localhost:8080`;

function fetchDataDetail(dataid) {
    fetch(`${API_URL}/data/${dataid}`, {
        headers: {
            'Cache-Control': 'no-cache'
        }
    })
        .then(res => res.json())
        .then(data => {
            showDataDetail(data);
        })
        .catch(error => {
            console.error(`Error Fetching details: ${error}`);
            document.getElementById('datadetail').innerHTML = 'Error Loading Data';
        });
}

function parseDataId() {
    try {
        var url_string = window.location.href.toLowerCase();
        var url = new URL(url_string);
        var dataid = url.searchParams.get('dataid');
        return dataid;
    } catch (err) {
        console.log("Issues with Parsing URL Parameter's - " + err);
        return '0';
    }
}

function showDataDetail(datadetail) {
    
    const ul = document.getElementById('datadetail');
    const detail = document.createDocumentFragment();
    console.log('Data:', datadetail);

    let li = document.createElement('div');
    let title = document.createElement('h2');
    let body = document.createElement('p');
    let by = document.createElement('p');
    
    title.innerHTML = `${datadetail.cycle_day}`;
    let temperature = document.createElement('p');
    let mood = document.createElement('p');
    let energy = document.createElement('p');
    let notes = document.createElement('p');

    temperature.innerHTML = `Temperature: ${datadetail.temperature}`;
    mood.innerHTML = `Mood: ${datadetail.mood}`;
    energy.innerHTML = `Energy: ${datadetail.energy}`;
    notes.innerHTML = `Notes: ${datadetail.notes}`;

    li.appendChild(title);
    li.appendChild(temperature);
    li.appendChild(mood);
    li.appendChild(energy);
    li.appendChild(notes);
  
 

    
    li.appendChild(body);
    li.appendChild(by);
    detail.appendChild(li);

    ul.appendChild(detail);
    }




function handlePage() {
    let dataid = parseDataId()
    console.log('dataid:', dataid);

    if (dataid != null) {
        console.log('found a dataid')
        fetchDataDetail(dataid);
    }
    
}
handlePage();