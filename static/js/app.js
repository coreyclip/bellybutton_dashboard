
// on initial page load
function initialize(){

    // create the dropdown menu
    DropDown();

    // set default pie chart
    let PieUrl = "/samples/BB_940";

    Plotly.d3.json(PieUrl, function(error, response){
        if (error) return console.warn(error);

        let data =[{
            values: Object.values(data.sample_values),
            labels: Object.values(data.otu_ids),
            type: "pie"
        }]


        Plotly.plot("piePlot", data)

    });

    // put the default values into the meta datatable
    var url_meta = "/metadata/BB_940";
    Plotly.d3.json(url_meta, function (error, metadata) {
        Plotly.d3.select("tbody").selectAll("tr")
            .data(metadata)
            .enter()
            .append("tr")
            .html(function (d) {
                return `<td>${Object.keys(d)}</td><td>${d[Object.keys(d)]}</td>`
            })
    });

    // initialize bubble chart
    let url_bubble = "/samples/BB_940";
    Plotly.d3.json(url_bubble, function(error, dataBubble){
        if (error) return console.warn(error)

        let data = [{
            x: Object.values(dataBubble.otu_ids),
            y: Object.values(dataBubble.sample_values),
            mode: 'markers', 
            marker: {
                size: Object.values(dataBubble.sample_values),
                color: Object.values(dataBubble.otu_ids)
            }
        }];

        let layout = {
            showlegend: True,
            xaxis:{
                title: "OTU ID"
            },
            yaxis:{
                title: "Sample values"
            },
            height: 800,
            width: 1300
        }

        Plotly.newPlot("bubble", data, layout)
    })

};




//retrieve names for dropdown 
function DropDown() {

    let url = "/sampleNames"

    let dropDownList = Plotly.d3.select("#selDataset").append('select')

    Plotly.d3.json(url, function(error, nameList){
        if (error) throw error;

        dropDownList.selectAll('option')
            .data(nameList)
            .enter()
            .append('option')
            .text(function (d) { return d; });
    });

}
// get data when dropdown selection changes

function getDataTable(sample_id) {
    var meta_url = "/metadata/" + sample_id;

    Plotly.d3.select("tbody").html("");

    Plotly.d3.json(meta_url, function (error, metaData) {
        Plotly.d3.select("tbody").selectAll("tr")
            .data(metaData)
            .enter()
            .append("tr")
            .html(function (d) {
                return `<td>${Object.keys(d)}</td><td>${d[Object.keys(d)]}</td>`
            })
    });


};


