fetch("./py_data.json")
  .then((res) => res.json())
  .then((data) => {
    console.log(data); 

    let myChart =  document.getElementById('myChart').getContext('2d');

    let chart = new Chart(myChart, {
        type:'bar', 
        data:{
            labels:[data[0].model, data[1].model, data[2].model, data[3].model],
            datasets:[{
                label:'Thinkpads',
                data:[
                    data[0].price_avg,
                    data[1].price_avg,
                    data[2].price_avg,
                    data[3].price_avg
                ],
                backgroundColor: 'red', 
                borderColor: 'black',
                borderWidth: 2 
            }]
        },
        options:{
            plugins: {
                legend: {
                    display: false, // legend still in progress
                    labels: {
                        font: {
                            size: 18, 
                            family: 'Arial'
                        },
                        color: 'white'
                    }
                }
            },
        backgroundColor: 'blue' // this does not work for some reason
        }
    });
});
