'use strict';
var width = 900;
var height = 400;
var t0 = Date.now();

var svg = d3.select('.container')
  .append('svg')
  .attr('width', width)
  .attr('height', height);

var planets = [
  { R: 100, r: 5, speed: 5, phi0: 90 }
];

var planets_2 = [
  { R: 150, r: 5, speed: 5, phi0: 90 }
];


var container = svg.append('g')
  .attr('transform', 'translate(' + width / 2 + ',' + height / 2 + ')');

container.selectAll('g.planet')
  .data(planets)
  .enter().append('g')
  .attr('class', 'planet')
  .each(function (d, i) {
    d3.select(this)
      .append("circle")
      .attr("class", "orbit")
      .attr("r", d.R);

    d3.select(this).append('circle')
      .attr('r', d.r)
      .attr('cx', d.R)
      .attr('cy', 0)
      .attr('class', 'planet');
  });

d3.timer(function () {
  var delta = Date.now() - t0;

  svg.selectAll('.planet')
    .attr('transform', function (d) {
    return 'rotate(' + d.phi0 + delta * d.speed / 200 + ')';
  });
});
