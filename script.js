fetch("./py_data.json")
  .then((res) => res.json())
  .then((data) => {
    console.log(data); 

    let myChart =  document.getElementById('myChart').getContext('2d');

    let chart = new Chart(myChart, {
        type:'line', 
        data:{
            labels:['5','6','7','8','9','10','11'],
            datasets:[{
                label:'Thinkpad 1',
                data:[
                    data[3].price_avg,
                    data[1].price_avg,
                    data[2].price_avg,
                    data[1].price_avg
                ],
                backgroundColor: 'red', 
                borderColor: 'black',
                borderWidth: 2 
            }, {
                label:'Thinkpad 2',
                data:[
                    data[2].price_avg,
                    data[1].price_avg,
                    data[3].price_avg,
                    data[1].price_avg
                ],
                backgroundColor: 'blue', 
                borderColor: 'black',
                borderWidth: 2 
            }, {
                label:'Thinkpad 3',
                data:[
                    data[2].price_avg,
                    data[3].price_avg,
                    data[3].price_avg,
                    data[1].price_avg
                ],
                backgroundColor: 'blue', 
                borderColor: 'black',
                borderWidth: 2 
            }]

        },
        options:{
            scales: {
                y: { 
                    beginAtZero: true,
                    ticks: {
                        stepSize: 50,
                        max: 400
                    },
                    title: {
                        display: true,
                        text: 'Price',
                        color: '#000',
                        font: {
                            size: 20
                        }
                    }
                },
                x: {
                    title: {
                        display: true,
                        text: 'July',
                        color: '#000',
                        font: {
                            size: 20
                        }
                    }
                }

            }
        }
    });
});
