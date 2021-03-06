var speedCanvas = document.getElementById("speedChart");

Chart.defaults.global.defaultFontFamily = "Lato";
Chart.defaults.global.defaultFontSize = 14;

var dataFirst = {
  label: "Four Years Ago",
  data: [30, 28, 26, 30, 32, 34, 33, 36, 40, 38, 39, 41],
  lineTension: 0,
  fill: false,
  borderColor: "red",
};

var dataSecond = {
  label: "Three Years Ago",
  data: [32, 29, 28, 35, 36, 35, 36, 34, 40, 42, 45, 46],
  lineTension: 0,
  fill: false,
  borderColor: "blue",
};
var dataThird = {
  label: "Two Years Ago",
  data: [36, 40, 34, 36, 38, 40, 42, 40, 40, 43, 44, 46],
  lineTension: 0,
  fill: false,
  borderColor: "green",
};
var dataFour = {
  label: "Last Year",
  data: [38, 41, 35, 43, 44, 46, 47, 45, 46, 47, 49, 50],
  lineTension: 0,
  fill: false,
  borderColor: "yellow",
};
var dataFive = {
  label: "This Year",
  data: [40, 41, 42, 43, 45, 48, 49, 50, 51, 52, 54],
  lineTension: 0,
  fill: false,
  borderColor: "orange",
};

var speedData = {
  labels: ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"],
  datasets: [dataFirst, dataSecond, dataThird, dataFour, dataFive],
};

var chartOptions = {
  legend: {
    display: true,
    position: "top",
    labels: {
      boxWidth: 40,
      fontColor: "black",
    },
  },
};

var lineChart = new Chart(speedCanvas, {
  type: "line",
  data: speedData,
  options: chartOptions,
});


