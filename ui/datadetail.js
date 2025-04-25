const API_URL = `http://localhost:8080`;

function fetchData() {
    fetch(`${API_URL}/data/<int:id>`, {
        headers: {
            'Cache-Control': 'no-cache'
        }
    })
        .then(res => res.json())
        .then(data => {
            showDataList(data);
        })
        .catch(error => {
            console.error(`Error Fetching entries: ${error}`);
            document.getElementById('data-list').innerHTML = 'Error Loading Data';
        });
}
