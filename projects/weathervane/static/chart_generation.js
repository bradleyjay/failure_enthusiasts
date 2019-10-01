console.log('D3 Time')
var formatted_actual_data = formatted_actual_data
var height = 1000
var width = 1000
console.log(formatted_actual_data)
// console.log(d3.min(formatted_actual_data, (d) => d[0]))

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
    .attr("height", height)
    .attr("width", width)

// render basic line
var x = d3.scaleLinear()
    .domain([d3.min(formatted_actual_data, (d) => d[0]), d3.max(formatted_actual_data, (d) => d[0])]) // data-scale coordinates of svg
    .range([0, width]);  // canvas-centric coordinates
var y = d3.scaleLinear()
    .domain([d3.min(formatted_actual_data, (d) => d[1]), d3.max(formatted_actual_data, (d) => d[1])])
    .range([height, 0]);

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

// svg.append("path")
//     .datum(retrieved_data)
//     .attr("fill", "none")
//     .attr("stroke", "steelblue")
//     .attr("stroke-width", 1.5)
//     .attr("d"
//         , d3.line()
//             .x((d) => x(d[0]))
//             .y((d) => y(d[1]))
//     )

svg.append("path")
    .datum(formatted_actual_data)
    .attr("fill", "none")
    .attr("stroke", "steelblue")
    .attr("stroke-width", 1.5)
    .attr("d"
        , d3.line()
            .x((d) => x(d[0]))
            .y((d) => y(d[1]))
    )
