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
        console.log(wfreqData[0]['WFREQ']);
        let wfreq = wfreqData[0]['WFREQ']
        const coef = 180 / 10;
        let level = coef * wfreq;
        
        // Trig to calc meter point
        let degrees = 180 - (level - 1);
        let radius = .5;

        let radians = degrees * Math.PI / 180;
        let x = radius * Math.cos(radians);
        let y = radius * Math.sin(radians);

        let mainPath = 'M -.0 -0.035 L .0 0.035 L ',
        pathX = String(x),
        space = ' ',
        pathY = String(y),
        pathEnd = ' Z';
 

        let path = mainPath.concat(pathX, space, pathY, pathEnd);

        data = [{
            type: 'scatter',
            x: [0], y: [0],
            marker: { size: 20, color: '#BF0803' },
            showlegend: false,
            name: 'Washing Frequency',
            text: wfreq,
            hoverinfo: 'text+name'
        },
        {
            values: [5 / 5, 5 / 5, 5 / 5, 5 / 5, 5 / 5, 5],
            rotation: 90,
            text: ['8-10', '6-8', '4-6', '2-4', '0-2', ''],
            textinfo: 'text',
            textposition: 'inside',
            marker: {
                colors: ['#459373', '#6EAB92',
                '#97C3B1', '#C1DBD0',
                '#EAF3EF',
                'rgb(255,255,255']
            },
            labels: ['8-10', '6-8', '4-6', '2-4', '0-2', ''],
            hoverinfo: 'label',
            hole: .5,
            type: 'pie',
            showlegend: false, 
            //sort: false
    }];

    var layout = {
        shapes: [{
            type: 'path',
            path: path,
            fillcolor: '850000',
            line: {
                color: '850000',
                weight: 1.5
            }
        }],

        height: 500,
        width: 400,
        xaxis: {
            zeroline: false, showticklabels: false,
            showgrid: false, range: [-1, 1]
        },
        yaxis: {
            zeroline: false, showticklabels: false,
            showgrid: false, range: [-1, 1]
        }
    };

    Plotly.newPlot('wfreq', data, layout);
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


        
