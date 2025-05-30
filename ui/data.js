const API_URL = `http://localhost:8080`;

function fetchData() {
    fetch(`${API_URL}/data`, {
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

function showDataList(data) {
    const DataListDiv = document.getElementById('data-list')
    DataListDiv.innerHTML = ''; // Clear any existing content
    const list = document.createDocumentFragment();

    data.map(function (data) {
         let div = document.createElement('div');
         let title = document.createElement('h3');
        // title.textContent = data.cycle_day || 'No Title';



        // let details = document.createElement('p');
        // details.textContent = `Rating ${entry.rating}`;

        // let genres = document.createElement('p');
        // genres.textContent = `Genres: ${entry.genres.join(', ')}`;

        let viewLink = document.createElement('a');
        viewLink.href = `/ui/datadetail.html?dataid=${data.id}`;
        viewLink.style = 'font-size: 20px; color: navy; text-decoration: none;';
        viewLink.onmouseover = () => viewLink.style.fontStyle = 'italic';
        viewLink.onmouseout = () => viewLink.style.fontStyle = 'normal';
        viewLink.textContent = data.cycle_day;

         div.appendChild(title);
         div.appendChild(viewLink);

         list.appendChild(div);
      
    });



    DataListDiv.appendChild(list);
    }



function handlePage() {
    console.log('load data detail');
    fetchData();
}

handlePage();