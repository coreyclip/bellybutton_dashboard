//retrieve names for dropdown 
function DropDown() {

    let url = "/sampleNames"

    let dropDownList = Plotly.d3.select("#selDataset")
                                

    Plotly.d3.json(url, function(error, nameList){
        if (error) throw error;

        dropDownList.selectAll('option')
            .data(nameList)
            .enter()
            .append('option')
            .text(function (d) { return d; });
    });

};
// get data when dropdown selection changes

function getDataTable(sample_id) {
    let meta_url = "/metadata/" + "BB_940";
    
    table = Plotly.d3.selectAll("tbody")

    Plotly.d3.json(meta_url, function (error, metaData) {
        if (error) console.warn(error);
        for (key in metaData){
            console.log(key, metaData[key])
            table.append('tr')
                 .html(`<td>${key}</td><td>${metaData[key]}</td>`)
                }
            });
    };
               
        

function PieChart(sample_id){
    let PieUrl = "/samples/" + sample_id;

    Plotly.d3.json(PieUrl, function(error, response){
        if (error) return console.warn(error);
        console.log(response)
        

        let trace =[{
            values: response.sample_values,
            labels: response.otu_ids,
            hoverinfo: 'label+percent+name',
            hole: .3,
            type: "pie"
        }]

        let layout = {
            title:`Sample ID: ${sample_id}`,
            height: 400,
            width: 500
          };

        Plotly.newPlot("piePlot", trace, layout)

    });
};

function bubblechart(sample_id){
    let url_bubble = "/samples/" + sample_id;
    Plotly.d3.json(url_bubble, function(error, dataBubble){
    if (error) return console.warn(error)

    let data = [{
        x: dataBubble.otu_id,
        y: dataBubble.sample_values,
        mode: 'markers', 
        marker: {
            size: dataBubble.sample_values,
            color: dataBubble.otu_ids
        }
    }];

    let layout = {
        showlegend: true,
        title:`Sample ID ${sample_id}`,
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
})};

// on initial page load
function initialize(){

    // create the dropdown menu
    DropDown();

    // load default MetaData table
    getDataTable("BB_940");

    // set default pie chart
    PieChart("BB_940");
    
    // initialize bubble chart
    bubblechart("BB_940")

};

initialize();

        
