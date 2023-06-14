/* Esta função recebe um url para poder buscas os dados */
function renderiza_faturamento_mensal(url) {

    fetch(url, {
        method: 'get',
    }).then(function (result) {
        return result.json()
    }).then(function (data) {

        const ctx = document.getElementById('faturamento_mensal').getContext('2d');
        var cores_faturamento_mensal = gera_cor(qtd = 12)
        const myChart = new Chart(ctx, {
            type: 'bar',
            data: {
                labels: data.labels,
                datasets: [{
                    label: "Faturamento",
                    data: data.data,
                    backgroundColor: cores_faturamento_mensal[0],
                    borderColor: cores_faturamento_mensal[1],
                    borderWidth: 1
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


    })

}