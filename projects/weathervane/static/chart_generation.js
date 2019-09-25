console.log('D3 Time')
var retrieved_data = retrieved_data
console.log(retrieved_data)

string_data = ["string1", "string2", "string3", "string4"]

numerical_data = [
    [0, 0]
    , [1, 1]
    , [2, 2]
    , [3, 3]
]

d3.select("#title")
    .style("font-size", "40px")

// create svg canvas
const svg = d3.select("div")
    .append("svg")
    .style("border", "solid red 1px")
    .attr("height", 100)
    .attr("width", 500)

// render basic line
var x = d3.scaleLinear()
    .domain([0, 3]) // data-scale coordinates of svg
    .range([0, 500]);  // canvas-centric coordinates
var y = d3.scaleLinear()
    .domain([0, 10])
    .range([100, 0]);

// draw line

// svg.append("path")
//     .datum(numerical_data)
//     .attr("fill", "none")
//     .attr("stroke", "steelblue")
//     .attr("stroke-width", 1.5)
//     .attr("d"
//         , d3.line()
//             .x((d) => x(d[0]))
//             .y((d) => y(d[1]))
//     )

svg.append("path")
    .datum(retrieved_data)
    .attr("fill", "none")
    .attr("stroke", "steelblue")
    .attr("stroke-width", 1.5)
    .attr("d"
        , d3.line()
            .x((d) => x(d[0]))
            .y((d) => y(d[1]))
    )
