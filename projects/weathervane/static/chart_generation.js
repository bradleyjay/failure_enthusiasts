console.log('actual_data')
var actual_data = actual_data
console.log(actual_data)
console.log('predictive_data')
var predictive_data = predictive_data
console.log(predictive_data)
var height = 700
var width = 700
var margin = 100
var legend_width = 200
var legend_height = 200
// console.log("BEFORE")
// console.log(formatted_data)

// error here - we assumed two series, predicive data will now only show up one hour into running the agent. SO, need to stop D3 from freaking out when it gets an empty [] instead of an array of arrays with data, for predictive_data specifically.

function createLineChart(actual_data, predictive_data, chart_title, y_axis_label, x_axis_label) {
    // Multiplying by 1000 since epochs are in milliseconds

    actual_data.forEach((d) => { d["time"] = d["time"] * 1000; })
    predictive_data.forEach((d) => { d["time"] = d["time"] * 1000; })
    // console.log("AFTER")
    // console.log(formatted_data)

    // sorting predictive data by time
    predictive_data.sort((x, y) => {
        return d3.ascending(x[0], y[0]);
    })

    // d3.selectAll("#chart")
    //     .attr("width", width)
    //     .style("border", "solid red 1px")

    d3.selectAll("#chart")
        .append("h2")
        .text(chart_title)

    // create svg canvas
    const svg = d3.select("#chart")
        .append("svg")
        .attr('viewBox', '0 0 ' + width + ' ' + height);
        // .attr("height", height)
        // .attr("width", width)

    // legend
    svg.append("g")
        .attr("id", "legend")
        .attr("transform", "translate(" + (width - legend_width) + ", 0)")
        .attr("height", legend_height)
        .attr("width", legend_width)

    // svg.append("rect")
    //     .attr("height", height - margin)
    //     .attr("width", width - margin)
    //     .attr("x", margin)
    //     .attr("y", 0)
    //     .style("border", "solid green 1px")

    // render basic line

    actual_x_min = d3.min(actual_data, (d) => d["time"])
    actual_x_max = d3.max(actual_data, (d) => d["time"])
    actual_y_max = d3.max(actual_data, (d) => d["temperature"])

    // bogus extreme values in case formatted_data isn't available

    if (predictive_data.length == 0) {
        predictive_x_min = 32529079406000
        predictive_x_max = -2183589394000
        predictive_y_max = -5000
    } else {
        predictive_x_min = d3.min(predictive_data, (d) => d["time"])
        predictive_x_max = d3.max(predictive_data, (d) => d["time"])
        predictive_y_max = d3.max(predictive_data, (d) => d["temperature"])
    }

    var x_min = Math.min(actual_x_min, predictive_x_min)

    var x_max = Math.max(actual_x_max, predictive_x_max)

    var y_max = Math.max(actual_y_max, predictive_y_max)

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

    var x_axis = d3.axisBottom(x).tickFormat(d3.timeFormat("%H:%M"))

    var y_axis = d3.axisLeft(y)

    function addLine(data_to_plot, line_color) {

        console.log("Data to Plot")
        // draw line
        // console.log('Function running!')
        // console.log(data_to_plot)

        // console.log('0th element!')
        // console.log(data_to_plot[0])
        // console.log('Error definitely incoming:')
        console.log(data_to_plot)
        svg.append("path")
            .datum(data_to_plot)
            .attr("fill", "none")
            .attr("stroke", line_color)
            .attr("stroke-width", 1.5)
            .attr("id", (d) => console.log("d0: " + x(d["time"]) + " d1: " + y(d["temperature"])))
            .attr("d"
                , d3.line()
                    .x((d) => x(d["time"]))
                    .y((d) => y(d["temperature"]))
            )

        d3.select("#legend")
            .append("rect")
            .attr("height", 15)
            .attr("width", 15)
            .attr("fill", line_color)

        d3.select("#legend")
            .append('text')
            .attr("transform", "translate(20,13.5)")
            .attr("height", 30)
            .attr("width", 100)
            .style("font-size", 15)
            .text("Hi or whatever")
        // Currently, next graph overwrites this block, hence why BLACK shows up, not RED
        // for next time, https://www.d3-graph-gallery.com/graph/custom_legend.html
    }

    addLine(actual_data, "red")

    if (predictive_data != []) {
        addLine(predictive_data, "black")
    }
    svg.append("g")
        .attr("transform", "translate(" + margin + ",0)")
        .call(y_axis)

    svg.append("g")
        .attr("transform", "translate(0," + (height - margin) + ")")
        .call(x_axis)

    svg.append("text")
        .attr("y", margin / 2)
        .attr("x", (-height + margin) / 2)
        .style("text-anchor", "middle")
        .text(y_axis_label)
        .attr("transform", "rotate(-90)")

    svg.append("text")
        .attr("y", height - (margin / 2))
        .attr("x", (margin + width) / 2)
        .style("text-anchor", "middle")
        .text(x_axis_label)

}


createLineChart(actual_data, predictive_data, "Predictive vs Actual Weather", "Degrees (F)", "Time")
