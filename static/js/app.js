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
    let meta_url = "/metadata/" + sample_id;
    
    table = Plotly.d3.selectAll("tbody")

    Plotly.d3.json(meta_url, function (error, metaData) {
        if (error) console.warn(error);
        table.selectAll('tr').remove();
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
            values: response[0].sample_values,
            labels: response[0].otu_ids,
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
        x: dataBubble[0].otu_id,
        y: dataBubble[0].sample_values,
        mode: 'markers', 
        marker: {
            size: dataBubble[0].sample_values,
            color: dataBubble[0].otu_ids
        }
    }];

    let layout = {
        showlegend: false,
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

function render_wfreq(sample_id){
    let wfreq_url = '/wfreq/' + sample_id;
    Plotly.d3.json(wfreq_url, function(error, wfreqData){
        if (error) console.warn(error);

        let data = [
            {
              y: [`sample: ${sample_id}`, 'The Sample Avg.'],
              x: [wfreqData[0][0],2.8],
              type: 'bar',
              orientation: "h",
            }
          ];

          layout = {
              title: "Washing Frequency per Week"
          }
        
          Plotly.newPlot('guage', data);
          
    });
};

// on initial page load
function initialize(){

    // create the dropdown menu
    DropDown();

    // load default MetaData table
    getDataTable("BB_940");

    // set default pie chart
    PieChart("BB_940");
    
    // initialize bubble chart
    bubblechart("BB_940");

    // initialize bar chart
    render_wfreq("BB_940");
};

initialize();

function optionChanged(sample_id){
    // create the dropdown menu
    DropDown();

    // load default MetaData table
    getDataTable(sample_id);

    // set default pie chart
    PieChart(sample_id);
    
    // initialize bubble chart
    bubblechart(sample_id);

    // initialize bar chart
    render_wfreq(sample_id);

}


        
