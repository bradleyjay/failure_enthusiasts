console.log('D3 Time')
var formatted_data = formatted_data
var height = 700
var width = 700
var margin = 100
console.log(formatted_data)


d3.select("#title")
    .style("font-size", "40px")

// create svg canvas
const svg = d3.select("div")
    .append("svg")
    .style("border", "solid red 1px")
    .attr("height", height)
    .attr("width", width)

// svg.append("rect")
//     .attr("height", height - margin)
//     .attr("width", width - margin)
//     .attr("x", margin)
//     .attr("y", 0)
//     .style("border", "solid green 1px")

// render basic line
var x_min = Math.min(d3.min(formatted_data[0], (d) => d[0]), d3.min(formatted_data[1], (d) => d[0]))

var x_max = Math.max(d3.max(formatted_data[0], (d) => d[0]), d3.max(formatted_data[1], (d) => d[0]))

var y_max = Math.max(d3.max(formatted_data[0], (d) => d[1]), d3.max(formatted_data[1], (d) => d[1]))

// console.log('x_min, x_max, y_max')
// console.log(x_min)
// console.log(x_max)
// console.log(y_max)

var x = d3.scaleLinear()
    .domain([x_min, x_max]) // data-scale coordinates of svg
    .range([margin, width]);  // canvas-centric coordinates

var y = d3.scaleLinear()
    .domain([0, y_max + 10])
    .range([height - margin, 0]);

var x_axis = d3.axisBottom(x)

var y_axis = d3.axisLeft(y)

function addLine(data_to_plot, line_color) {
    // draw line
    // console.log('Function running!')
    // console.log(data_to_plot)

    // console.log('0th element!')
    // console.log(data_to_plot[0])
    // console.log('Error definitely incoming:')
    svg.append("path")
        .datum(data_to_plot)
        .attr("fill", "none")
        .attr("stroke", line_color)
        .attr("stroke-width", 1.5)
        .attr("id", (d) => console.log(d[0]))
        .attr("d"
            , d3.line()
                .x((d) => x(d[0]))
                .y((d) => y(d[1]))
        )
}

addLine(formatted_data[0], "red")
addLine(formatted_data[1], "black")
svg.append("g")
    .attr("transform", "translate(" + margin + ",0)")
    .call(y_axis)

svg.append("g")
    .attr("transform", "translate(0," + (height - margin) + ")")
    .call(x_axis)

