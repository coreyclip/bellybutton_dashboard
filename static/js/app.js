


//retrieve names for dropdown 
function DropDown() {

    let url = "/sampleNames"

    let dropDownList = Plotly.d3.select("#selDataset")

    Plotly.d3.json(url, function(error, nameList){
        if (error) throw error;

        dropDownList..selectAll('option')
            .data(nameList)
            .enter()
            .append('option')
            .text(function (d) { return d; });
    });

}
// get data when dropdown selection changes

function getData(sample_id) {
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


}
