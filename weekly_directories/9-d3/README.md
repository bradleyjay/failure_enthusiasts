# What is d3?
[D3](https://d3js.org/) is a Javascript library for creating nifty [interactive] visualizations

# Key concepts
## Including the library
Add this in the head of your HTML:
```
<script src="https://d3js.org/d3.v4.min.js"></script>
```

## Selecting
- `d3.select([id/class/element/etc])` to select the first element that meets the criteria
- `d3.selectAll([id/class/element/etc])` to select all elements that meet the criteria

## Adding data
```
.data([dataset])
.enter()
.append([type of element])
```

## Using that data to do something
You can reference your data in all sorts of calls - changing the location/size of shapes, colors, text, etc. Some examples:
```
.attr("height", (d) => d)
.attr("y", (d) => svg_height - d)
.text((d) => d)
```

## Bar charts
Must have x, y, width, and height attributes. Note that the y-axis behaves the opposite way you might expect. 0 on the y-axis is the top of the chart.

Example:
```
svg.selectAll("rect")
   .data(numerical_data)
   .enter()
   .append("rect")
   .attr("x", (d,i)=>21*i)
   .attr("y", (d)=>100 - (d[0]*10))
   .attr("width", 20)
   .attr("height", (d)=>d[0]*10) ;
```

## Scatterplot/circles
Circle objects must have cx, cy, and r attributes

Example:
```
svg.selectAll("circle")
  .data(numerical_data)
  .enter()
  .append("circle")
  .attr("cx", (d,i)=>d[0]*50)
  .attr("cy", (d)=>100 - (d[0]*10))
  .attr("r", 10)
  .style("opacity", .2)
  .style("stroke", "black")
  .style("stroke-width", "2px")
  .style("fill", "green");
```

## Line charts
Define axis scales then call the axis scales in the d attribute

Example:
```
var x = d3.scaleLinear()
      .domain([0,3])
      .range([0,500]);
var y = d3.scaleLinear()
      .domain([0, 3])
      .range([100, 0]);

svg.append("path")
      .datum(numerical_data)
      .attr("fill", "none")
      .attr("stroke", "steelblue")
      .attr("stroke-width", 1.5)
      .attr("d"
              , d3.line()
                  .x((d)=>x(d[0]))
                  .y((d)=>y(d[1]))
           )
```

# Other resources
[Udemy course](https://datadog.udemy.com/course/learn-d3js-for-data-visualization/) if you want to get a pretty detailed understanding

[FreeCodeCamp D3 lessons](https://learn.freecodecamp.org/data-visualization/data-visualization-with-d3): play around with simple examples in-browser
