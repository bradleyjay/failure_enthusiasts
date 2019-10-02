console.log('D3 Time')
var formatted_actual_data = formatted_actual_data
var height = 700
var width = 700
var margin = 100
console.log(formatted_actual_data)


d3.select("#title")
    .style("font-size", "40px")

// create svg canvas
const svg = d3.select("div")
    .append("svg")
    .style("border", "solid red 1px")
    .attr("height", height)
    .attr("width", width)

svg.append("rect")
    .attr("height", height - margin)
    .attr("width", width - margin)
    .attr("x", margin)
    .attr("y", 0)
    .style("border", "solid green 1px")

// render basic line
var x = d3.scaleLinear()
    .domain([d3.min(formatted_actual_data, (d) => d[0]), d3.max(formatted_actual_data, (d) => d[0])]) // data-scale coordinates of svg
    .range([margin, width]);  // canvas-centric coordinates
var y = d3.scaleLinear()
    .domain([0, d3.max(formatted_actual_data, (d) => d[1]) + 10])
    .range([height - margin, 0]);

var x_axis = d3.axisBottom(x)

var y_axis = d3.axisLeft(y)

// draw line
svg.append("path")
    .datum(formatted_actual_data)
    .attr("fill", "none")
    .attr("stroke", "white")
    .attr("stroke-width", 1.5)
    .attr("d"
        , d3.line()
            .x((d) => x(d[0]))
            .y((d) => y(d[1]))
    )

svg.append("g")
    .attr("transform", "translate("+margin+",0)")
    .call(y_axis)

svg.append("g")
    .attr("transform", "translate(0,"+(height-margin)+")")
    .call(x_axis)