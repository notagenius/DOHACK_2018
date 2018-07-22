(function(){
  "use strict";

  var w = 720;
  var h = 487;

  //スケールの指定
  var xscale = d3.scale.linear()
           .domain([0,50.0])
           .range([0, w]);
           
  var yscale = d3.scale.linear()
           .domain([0,33.79])
           .range([0, h]);

  //初期化              
  var map = d3.floorplan().xScale(xscale).yScale(yscale);
  var imagelayer = d3.floorplan.imagelayer();
  var heatmap = d3.floorplan.heatmap();
  var pathplot = d3.floorplan.pathplot();
  var overlays = d3.floorplan.overlays().editMode(true);
  var mapdata = {};

  //ベースとなる画像データの読み込み
  mapdata[imagelayer.id()] = [{
    url: 'images/map.png',
    x: 0,
    y: 0,
    height: 33.79,
    width: 50.0
  }];

  //レイヤーの追加    
  map.addLayer(imagelayer)
    .addLayer(heatmap)
    .addLayer(pathplot)
    .addLayer(overlays);
     
  //ポリゴン、ヒートマップ、パスデータの読み込み   
  d3.json("data/data.json", function(data) {
    mapdata[heatmap.id()] = data.heatmap;
    mapdata[overlays.id()] = data.overlays;
    mapdata[pathplot.id()] = data.pathplot;

    //フロアマップ表示
    d3.select("#demo").append("svg")
                      .attr("width", w)
                      .attr("height", h)
                      .datum(mapdata)
                      .call(map);
  });
})();
