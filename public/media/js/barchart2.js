var h=300;
var w=700;
var margin = {"top":20,"bottom":20,"left":200,"right":20}
var height=h-margin.top-margin.bottom;
var width = w- margin.right-margin.left;
//var data = [23, 85, 67, 38, 70, 30, 80, 90 ];
//var data = "{{ data }}";
var labellist  = (document.getElementById("myVar1").value);
var data = (document.getElementById("myVar3").value)
var data = JSON.parse(data)
var labellist = ['E','G']
var colorlist = ["maroon", "darkblue"];

//var labellist = ["Perso1", "Person2", "Person3", "Person4", "Person5", "Person6", "Person7", "Hao"];
//var labellist = "{{ label }}";

var x=d3.scale.linear().domain([0,d3.max(data)]).range([0,width]);

var y= d3.scale.ordinal()
	.domain(d3.range(data.length))
	.rangeBands([height,0],0.15);

var svg = d3.select("div.barchart2")
  .append("svg:svg")
    .attr("width", w )
    .attr("height", h)
    .append("svg:g")
    .attr("transform", "translate("+margin.left+","+margin.top+")");

var xAxis = d3.svg.axis()
	.scale(x)
	.ticks(10)
	.tickSize(-height)
	.orient("bottom")
	.tickFormat(function(d){return d});
	
	svg.append("g")
	.attr("class","x axis")
	.attr("transform","translate(0,"+height+")")
	.call(xAxis);

var yAxis = d3.svg.axis()
	.scale(y)
	.orient("left")
	.tickSize(-width)
	;
var gy=svg.append("g")
	.attr("class","y axis")
	.call(yAxis)

	gy.selectAll("text")
	.text(function(d){ return labellist[d]})
	.attr("x",-10)
	.attr("dy","0.5em")
	.style("font-size",16);

	gy.selectAll("line")
    .style("stroke","red");

var title = svg.append("text")
	.text("Plc consumption by commodityid ")
	.attr("x",-200)
	.attr("y",-100)
	.attr("class","title")
	;
var bars = svg.selectAll(".bar")
	.data(data)
	.enter()
	
	bars.append("rect")
	.attr("class",function(d) {
		if(d>50) {return "bar-less"}
		else{return "bar-more"}		
	})
	.attr("transform",function(i,d){return "translate("+0+","+y.range()[d]+")"})
	.attr("width",function(d){return width/d3.max(data)*d})
	.attr("height",(y.rangeBand()))
	.on('mouseover', tipshide)
    .on('mouseout', tipsshow)
;
	bars.append("text")
	.attr("class","bar-text")
	.text(function(d) {return d })
	.attr("x",function(d){return 80*d})
	.attr("dy","2em")
	.attr("dx","-2em")
	.attr("transform",function(i,d){return "translate("+0+","+y.range()[d]+")"})
;

function tipsshow(){
	d3.selectAll(".bar-text")
	.style("display","none");
}
function tipshide(){
	d3.selectAll(".bar-text")
	.style("transition","2s")
	.style("display","inline")
;
}
