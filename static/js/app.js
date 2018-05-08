
// on initial page load
function initialize(){

    // create the dropdown menu
    DropDown();

    // set default pie chart
    let PieUrl = "/samples/BB_941";

    Plotly.d3.json(PieUrl, function(error, response){
        if (error) return console.warn(error);
        //console.log(response)
        

        let trace =[{
            values: response.sample_values,
            labels: response.otu_ids,
            type: "pie"
        }]


        Plotly.plot("piePlot", trace)

    });

    // put the default values into the meta datatable
    let url_meta = "/metadata/BB_940";
    Plotly.d3.json(url_meta, function (error, metadata) {
        if (error) console.warn(error);
        
        Plotly.d3.select("tbody")
            .selectAll("tr")
            .data(metadata)
            .enter()
            .append("tr")
            .html(function (obj) {for (key in obj){
                console.log(key, obj[key])
                return `<td>${key}</td><td>${obj[key]}</td>`
            };
                
            });
    });

    // initialize bubble chart
    let url_bubble = "/samples/BB_940";
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

initialize()


