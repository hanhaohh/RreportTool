
// Set the dimensions of the canvas / graph
var margin = {top: 50, right:20, bottom: 20, left: 20},
    width = 600 - margin.left - margin.right,
    height = 400 - margin.top - margin.bottom;

// Parse the date / time
var parseDate = d3.time.format("%d-%b-%y").parse;

// Set the ranges
var x = d3.time.scale().range([0, width]);
var y = d3.scale.linear().range([height, 0]);

// Define the axes
var xAxis = d3.svg.axis().scale(x)
    .orient("bottom").ticks(5)
;

var yAxis = d3.svg.axis().scale(y)
    .orient("left").ticks(5);

// Define the line
var valueline = d3.svg.line()
    .x(function(d) { return x(d.date); })
    .y(function(d) { return y(d.close); });

// Adds the svg canvas
var svg = d3.select("body")
    .append("svg")
        .attr("width", 1200 + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
        .append("g")
        .attr("transform","translate(" + 300 + "," + margin.top + ")")
        ;
svg.append("text")
.attr("x", 500)
.attr("y", -10)
.attr("font-size","20px")
.attr("fill","#58FAF4")
.text("Works From Jan 2013 - Sep 2014");

/* Initialize tooltip */
tip = d3.tip().html(function(d) { return "<h5>Click to see the project</h5>"    ; });

/* Invoke the tip in the context of your visualization */
svg.call(tip);

// Get the data
d3.csv("/media/data/data.csv", function(error, data) {
    data.forEach(function(d) {
        d.date = parseDate(d.date);
        d.close = +d.close;
        d.url=d.url;
        d.name=d.name;
        d.yanse = d.yanse;
    });

    // Scale the range of the data
    x.domain(d3.extent(data, function(d) { return d.date; }));
    y.domain([0, d3.max(data, function(d) { return d.close; })]);

    // Add the valueline path.
    // Add the scatterplot

    svg.selectAll("text")
    .data(data)
    .enter()
    .append("text")
    .attr("x", function(d) { return x(d.date)-30; })
    .attr("y", function(d) { return y(d.close)-20; })
    .text(function(d){return d.name});

    svg.selectAll("dot")
    .data(data)
    .enter()
    .append("a")
    .attr("xlink:href",function(d){return (d.url)})
    .append("circle")
    .attr("cx", function(d) { return x(d.date); })
    .attr("cy", function(d) { return y(d.close); })
    .attr("r", 15)
    .style("fill", function(d) {return d.yanse})
    .style("opacity", 1)
    .on('mouseover', tip.show)
    .on('mouseout', tip.hide);

    // Add the X Axis
    svg.append("g")
        .attr("class", "x axis")
        .attr("transform", "translate(0," + height + ")")
        .call(xAxis);

    // Add the Y Axis
    svg.append("g")
        .attr("class", "y axis")
        .call(yAxis);

});

