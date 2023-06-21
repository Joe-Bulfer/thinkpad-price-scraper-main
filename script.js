const fs = require('fs')

fs.readFile('py_data.json', 'utf8', (err,jsonString) => {
    if (err) {
        console.error('Errorreading file', err);
        return;
    }

    try {
        const data = JSON.parse(jsonString);

        console.log(data[4]);
    } catch (err) {
        console.error('Error parsing JSON', err);
    }
});

function sendRequest() {
    // const searchBar = document.getElementById("search-bar");
    // const data = { searchText: searchBar.value };
    data = "test" 
    fs.writeFileSync('js_data.json', JSON.stringify(data));
}
