// const fs = require('fs')

// fs.readFile('py_data.json', 'utf8', (err,jsonString) => {
//     if (err) {
//         console.error('Errorreading file', err);
//         return;
//     }

//     try {
//         const data = JSON.parse(jsonString);

//         console.log(data[4]);
//     } catch (err) {
//         console.error('Error parsing JSON', err);
//     }
// });

// function sendRequest() {
//     // const searchBar = document.getElementById("search-bar");
//     // const data = { searchText: searchBar.value };
//     data = "test" 
//     fs.writeFileSync('js_data.json', JSON.stringify(data));
// }

let myChart =  document.getElementById('myChart').getContext('2d');

// Filling in arbitrary data until scrape.py works
let chart = new Chart(myChart, {
    type:'bar', // can be bar, horixontal bar, etc.
    data:{
        labels:['x230','t410','t430','t480',],
        datasets:[{
            label:'Thinkpads',
            data:[
                340,
                230,
                190,
                250
            ]
        }]
    },
    options:{}
});
