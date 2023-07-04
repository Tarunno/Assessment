getStats()

async function getStats(){
  const res =  await fetch('/admin/update-thread/')
  const dataset = await res.json()

  const ctx = document.getElementById('myChart');
  let labels = dataset.time.map((x) => x.split('T').join(' ').split('.')[0].split(' '))
  console.log(labels);

  await new Chart(ctx, {
    type: 'line',
    data: {
      labels: labels,
      datasets: [{
        label: 'Auction added',
        data: dataset.auction_added,
        borderWidth: 1,
        fill: true
      },
      {
        label: 'Auction completed',
        data: dataset.auction_ended,
        borderWidth: 1,
        fill: true
      }]
    },
    options: {
      scales: {
        y: {
          beginAtZero: true
        }
      }
    }
  });
  const ctx2 = document.getElementById('myChart2');
  let labels2 = dataset.time.map((x) => x.split('T').join(' ').split('.')[0].split(' '))
  console.log(labels2);

  await new Chart(ctx2, {
    type: 'line',
    data: {
      labels: labels2,
      datasets: [{
        label: 'Auction value',
        data: dataset.value,
        borderWidth: 1,
        fill: true
      }]
    },
    options: {
      scales: {
        y: {
          beginAtZero: true
        }
      }
    }
  });
} 