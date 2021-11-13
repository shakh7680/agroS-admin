var barChartData = {
    labels: [
      "Last 4 year",
      "Last 3 year",
      "Last 2 yera",
      "Last year",
      "This year",
    ],
    datasets: [
      {
        label: "$ Invested",
        backgroundColor: "pink",
        borderColor: "red",
        borderWidth: 1,
        data: [3, 5, 6, 10, 8 ]
      },
      {
        label: "$ Resturned",
        backgroundColor: "lightblue",
        borderColor: "blue",
        borderWidth: 1,
        data: [4, 7, 7, 10, 15 ]
      }
    ]
  };
  
  var chartOptions = {
    responsive: true,
    legend: {
      position: "top"
    },
    title: {
      display: true,
      text: "Past 5 year information"
    },
    scales: {
      yAxes: [{
        ticks: {
          beginAtZero: true
        }
      }]
    }
  }
  
  window.onload = function() {
    var ctx = document.getElementById("canvas").getContext("2d");
    window.myBar = new Chart(ctx, {
      type: "bar",
      data: barChartData,
      options: chartOptions
    });
  };
  